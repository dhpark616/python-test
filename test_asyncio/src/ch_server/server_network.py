import asyncio
import logging
import time
from socket import TCP_NODELAY, IPPROTO_TCP

from .actor import player as actor_player
from .conns import CONN_IDX, CONNS
from .handler_dict import HANDLER, PACKET_TYPE_CLASS_DICT
from .players import PLAYERS
from .. import e
from ..msg import msg_type_ch_pb2
from ..msg.msg import HEADER_SIZE, unpack_header, unpack_body
from ..util import protobuf_to_dict


class TCPServerConnection(asyncio.Protocol):
    def __init__(self):
        self.conn_idx = 0
        self.transport = None
        self.msg_buffer = b''

    def connection_made(self, transport):
        self.conn_idx = CONN_IDX.get_next_idx()
        self.transport = transport
        sock = self.transport.get_extra_info('socket')
        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)

        CONNS.add(self.conn_idx, self)
        handle_received(self.conn_idx, e.CREATE_PLAYER, None)

    def data_received(self, data):
        self.msg_buffer += data
        msg_header_idx = 0
        while len(self.msg_buffer) >= msg_header_idx + HEADER_SIZE:
            msg_type, msg_idx, msg_size = unpack_header(self.msg_buffer, msg_header_idx)

            if len(self.msg_buffer) < msg_idx + msg_size:
                break

            msg_str = unpack_body(self.msg_buffer, msg_idx, msg_size)
            handle_received(self.conn_idx, msg_type, msg_str)

            msg_header_idx = msg_idx + msg_size

        self.msg_buffer = self.msg_buffer[msg_header_idx:]

    def eof_received(self):
        pass

    def connection_lost(self, exc):
        handle_received(self.conn_idx, e.DELETE_PLAYER, None)


def is_normal_packet(msg_type):
    system_packets = [
        e.CREATE_PLAYER,
        e.DELETE_PLAYER,
        msg_type_ch_pb2.t_load_char_req
    ]

    if msg_type not in system_packets:
        return True
    return False


def handle_received(conn_idx, msg_type, msg_str):
    func = HANDLER[msg_type]
    if func is None:
        return

    if msg_type == e.CREATE_PLAYER:
        player = actor_player.Player(conn_idx)
        PLAYERS.add(conn_idx, player)
    else:
        if conn_idx not in PLAYERS:
            return
        player = PLAYERS[conn_idx]

    if is_normal_packet(msg_type):
        if not player.is_loaded:
            return

    start_time = time.time()

    async def run_handler():
        try:
            req = None
            if msg_type in PACKET_TYPE_CLASS_DICT:
                req = PACKET_TYPE_CLASS_DICT[msg_type]()
                req.ParseFromString(msg_str)

            if asyncio.iscoroutinefunction(func):
                await func(player, req)
            else:
                func(player, req)

            latency = round(time.time() - start_time, 4)
            extra = {
                "conn_idx": conn_idx,
                "msg_type": get_enum_name(msg_type),
                "req": protobuf_to_dict(req),
                "latency": latency,
            }
            logging.info('recv', extra=extra)
        except Exception as e:
            extra = {
                "conn_idx": conn_idx,
                "msg_type": get_enum_name(msg_type),
            }
            logging.exception(repr(e), extra=extra)

    asyncio.ensure_future(run_handler())


def get_enum_name(msg_type):
    if msg_type in PACKET_TYPE_CLASS_DICT:
        return msg_type_ch_pb2.type_ch.get_enum_name(msg_type)
    return e.get_enum_name(msg_type)
