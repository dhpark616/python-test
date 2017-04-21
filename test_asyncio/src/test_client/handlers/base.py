import logging

from ..conns import CONNS
from ..handler_dict import HANDLER
from ..players import PLAYERS
from ... import e
from ...msg import msg_type_ch_pb2, msg_packet_ch_pb2, msg_error_pb2
from ...util import protobuf_to_dict


@HANDLER.msg_id(e.CREATE_PLAYER)
def h_create_player(player, _):
    logging.info('create_player', extra={'player': repr(player)})

    req = msg_packet_ch_pb2.load_char_req()
    req.auth_token = 'asjfdlasjfljsalfd'
    req.char_idx = 100
    player.send(req)


@HANDLER.msg_id(e.DELETE_PLAYER)
def h_delete_player(player, _):
    logging.info('delete_player', extra={'player': player})
    conn_idx = player.conn_idx
    PLAYERS.remove(conn_idx)
    CONNS.remove(conn_idx)


@HANDLER.msg_id(msg_type_ch_pb2.t_load_char_ack)
def h_load_char_ack(player, ack):
    logging.info('load_char', extra={'player': player})

    if ack.err_code != msg_error_pb2.err_none:
        logging.info('h_load_char_ack', extra=protobuf_to_dict(ack))
        return

    player.server_char_idx = ack.conn_idx
