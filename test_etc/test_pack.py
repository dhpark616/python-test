import struct
import json

_header_size = 6


def pack_packet(msg):
    msg_type = msg['msg_type']
    msg_str = json.dumps(msg)
    msg_bytes = bytes(msg_str, encoding='utf-8')
    packed = struct.pack('HHBB', msg_type, len(msg_bytes), 0, 0) + msg_bytes
    return packed


def unpack_header(msg_buffer, msg_header_idx):
    msg_idx = msg_header_idx + _header_size
    msg_type, msg_size, _, _ = struct.unpack('HHBB', msg_buffer[msg_header_idx:msg_idx])
    return msg_type, msg_idx, msg_size


def unpack_body(msg_buffer, msg_idx, msg_size):
    msg_next_header_idx = msg_idx + msg_size
    msg_bytes = msg_buffer[msg_idx:msg_next_header_idx]
    msg_str = str(msg_bytes, encoding='utf-8')
    msg = json.loads(msg_str)
    return msg


def main():
    msg_buffer = b''
    for i in range(5):
        msg = dict()
        msg['msg_type'] = 10000 + i
        msg['dungeon_mid'] = 20000 + i

        packed = pack_packet(msg)
        print(packed)
        msg_buffer += packed
    
    # 짤린 버퍼 테스트용 코드
    remain_msg_buffer = msg_buffer[-10:]
    print(remain_msg_buffer)
    msg_buffer = msg_buffer[:-10]
    print(msg_buffer)

    msg_header_idx = 0
    while len(msg_buffer) >= msg_header_idx + _header_size:
        msg_type, msg_idx, msg_size = unpack_header(msg_buffer, msg_header_idx)
        print(msg_type, msg_idx, msg_size)

        # body가 짤린 경우
        if len(msg_buffer) < msg_idx + msg_size:
            break

        unpack_msg = unpack_body(msg_buffer, msg_idx, msg_size)
        print(unpack_msg)

        msg_header_idx = msg_idx + msg_size
        print(msg_header_idx)

    # 처리된 데이터 삭제
    msg_buffer = msg_buffer[msg_header_idx:]
    print(msg_buffer)

    # 남은 데이터가 완성되었을 때 처리
    msg_buffer += remain_msg_buffer

    msg_header_idx = 0
    while len(msg_buffer) >= msg_header_idx + _header_size:
        msg_type, msg_idx, msg_size = unpack_header(msg_buffer, msg_header_idx)
        print(msg_type, msg_idx, msg_size)

        # body가 짤린 경우
        if len(msg_buffer) < msg_idx + msg_size:
            break

        unpack_msg = unpack_body(msg_buffer, msg_idx, msg_size)
        print(unpack_msg)

        msg_header_idx = msg_idx + msg_size
        print(msg_header_idx)

    # 처리된 데이터 삭제
    msg_buffer = msg_buffer[msg_header_idx:]
    print(msg_buffer)


if __name__ == '__main__':
    main()




