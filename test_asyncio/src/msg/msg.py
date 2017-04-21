import struct
import json

# header == msg_type(2 bytes), msg_size(2 bytes), identity(1 byte), sequence(1 byte)
HEADER_SIZE = 6


def pack_packet(msg_type, msg):
    msg_str = msg.SerializeToString()
    packed = struct.pack('HHBB', msg_type, len(msg_str), 0, 0) + msg_str
    return packed


def unpack_header(msg_buffer, msg_header_idx):
    msg_idx = msg_header_idx + HEADER_SIZE
    msg_type, msg_size, _, _ = struct.unpack('HHBB', msg_buffer[msg_header_idx:msg_idx])
    return msg_type, msg_idx, msg_size


def unpack_body(msg_buffer, msg_idx, msg_size):
    msg_next_header_idx = msg_idx + msg_size
    msg_str = msg_buffer[msg_idx:msg_next_header_idx]
    return msg_str
