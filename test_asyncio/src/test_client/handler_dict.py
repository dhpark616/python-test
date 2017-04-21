from ..msg import msg_packet_ch_pb2
from ..msg import msg_type_ch_pb2

PACKET_CLASS_TYPE_DICT = {}
for i in dir(msg_packet_ch_pb2):
    find_name = 't_' + i
    for j in dir(msg_type_ch_pb2):
        if find_name == j:
            PACKET_CLASS_TYPE_DICT[getattr(msg_packet_ch_pb2, i)] = getattr(msg_type_ch_pb2, find_name)
            break

PACKET_TYPE_CLASS_DICT = {v: k for k, v in PACKET_CLASS_TYPE_DICT.items()}

PACKET_REQ_ACK_DICT = {}
for i in PACKET_CLASS_TYPE_DICT.keys():
    if '_req' not in i.__name__:
        continue
    find_name = i.__name__.replace('_req', '_ack')
    for j in dir(msg_packet_ch_pb2):
        if find_name == j:
            PACKET_REQ_ACK_DICT[i] = getattr(msg_packet_ch_pb2, find_name)
            break

PACKET_ACK_REQ_DICT = {v: k for k, v in PACKET_REQ_ACK_DICT.items()}


class Handler(dict):
    def __init__(self):
        self.func_map = {}
        super().__init__()

    def msg_id(self, msg_type):
        def func_wrapper(func):
            self.func_map[msg_type] = func
            return func

        return func_wrapper

    def __getitem__(self, item):
        return self.func_map.get(item, None)


HANDLER = Handler()
