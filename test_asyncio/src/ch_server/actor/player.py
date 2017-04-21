import logging

from ..handler_dict import PACKET_CLASS_TYPE_DICT
from ...msg.msg import pack_packet
from ...msg import msg_type_ch_pb2
from ...util import protobuf_to_dict
from ..conns import CONNS


class Player:
    def __init__(self, conn_idx):
        self.conn_idx = conn_idx
        self.is_loaded = False

    def __repr__(self):
        return str({'conn_idx': self.conn_idx, 'is_loaded': self.is_loaded})

    def send(self, ack):
        msg_type = PACKET_CLASS_TYPE_DICT[type(ack)]
        try:
            msg = pack_packet(msg_type, ack)
            extra = {
                "conn_idx": self.conn_idx,
                "msg_type": msg_type_ch_pb2.type_ch.get_enum_name(msg_type),
                "ack": protobuf_to_dict(ack),
            }
            logging.info('send', extra=extra)
            CONNS.send(self.conn_idx, msg)
        except Exception as e:
            extra = {
                "conn_idx": self.conn_idx,
                "msg_type": msg_type_ch_pb2.type_ch.get_enum_name(msg_type),
            }
            logging.exception(repr(e), extra=extra)


