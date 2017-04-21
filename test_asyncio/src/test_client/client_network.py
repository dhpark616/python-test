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

CLIENTS = []


class TCPClientConnection(asyncio.Protocol):
    def __init__(self, user_id, char_name):
        self.conn_idx = 0
        self.transport = None
        self.msg_buffer = b''
        self.user_id = user_id
        self.char_name = char_name

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


def connect(loop, host, port, user_id, char_name):
    try:
        coro = loop.create_connection(lambda: TCPClientConnection(user_id, char_name), host, port)
        client = asyncio.ensure_future(coro)
        client.loop = loop
        client._closing = False
        CLIENTS.append(client)
        logging.info('connect', extra={'host': host, 'port': port, 'user_id': user_id, 'char_name': char_name})
    except Exception as err:
        logging.exception(err)


def disconnect(conn_idx):
    try:
        conn = CONNS[conn_idx]
        conn.transport.close()
        logging.info('disconnect', extra={'conn_idx': conn_idx, 'user_id': conn.user_id, 'char_name': conn.char_name})
    except Exception as err:
        logging.exception(err)


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

    start_time = time.time()

    async def run_handler():
        try:
            ack = None
            if msg_type in PACKET_TYPE_CLASS_DICT:
                ack = PACKET_TYPE_CLASS_DICT[msg_type]()
                ack.ParseFromString(msg_str)

            if asyncio.iscoroutinefunction(func):
                await func(player, ack)
            else:
                func(player, ack)

            latency = round(time.time() - start_time, 4)
            extra = {
                "conn_idx": conn_idx,
                "msg_type": get_enum_name(msg_type),
                "ack": protobuf_to_dict(ack),
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
