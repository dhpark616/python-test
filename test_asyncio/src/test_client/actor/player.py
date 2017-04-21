import logging

from ..handler_dict import PACKET_CLASS_TYPE_DICT
from ...msg.msg import pack_packet
from ...msg import msg_type_ch_pb2
from ...util import protobuf_to_dict
from ..conns import CONNS


class Player:
    def __init__(self, conn_idx):
        self.conn_idx = conn_idx
        self.server_conn_idx = 0

    def __repr__(self):
        return {"conn_idx": self.conn_idx, "server_conn_idx": self.server_conn_idx}.__str__()

    def send(self, req):
        msg_type = PACKET_CLASS_TYPE_DICT[type(req)]
        try:
            msg = pack_packet(msg_type, req)
            extra = {
                "conn_idx": self.conn_idx,
                "msg_type": msg_type_ch_pb2.type_ch.get_enum_name(msg_type),
                "ack": protobuf_to_dict(req),
            }
            logging.info('send', extra=extra)
            CONNS.send(self.conn_idx, msg)
        except Exception as e:
            extra = {
                "conn_idx": self.conn_idx,
                "msg_type": msg_type_ch_pb2.type_ch.get_enum_name(msg_type),
            }
            logging.exception(repr(e), extra=extra)


