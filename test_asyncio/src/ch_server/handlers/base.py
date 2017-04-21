import logging

from ..conns import CONNS
from ..handler_dict import HANDLER
from ..players import PLAYERS
from ... import e
from ...msg import msg_type_ch_pb2, msg_packet_ch_pb2, msg_error_pb2


@HANDLER.msg_id(e.CREATE_PLAYER)
def h_create_player(player, _):
    logging.info('create_player', extra={'player': player})


@HANDLER.msg_id(e.DELETE_PLAYER)
def h_delete_player(player, _):
    logging.info('delete_player', extra={'player': player})
    conn_idx = player.conn_idx
    PLAYERS.remove(conn_idx)
    CONNS.remove(conn_idx)


@HANDLER.msg_id(msg_type_ch_pb2.t_load_char_req)
def h_load_char_req(player, req):
    logging.info('load_char', extra={'player': player})
    if player.is_loaded:
        return

    player.char_idx = req.char_idx
    player.is_loaded = True

    ack = msg_packet_ch_pb2.load_char_ack()
    ack.err_code = msg_error_pb2.err_none
    ack.conn_idx = player.conn_idx
    player.send(ack)
