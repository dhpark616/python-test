from enum import IntEnum


class MsgTypeInternal(IntEnum):
    CREATE_PLAYER = 1
    DELETE_PLAYER = 2


MSG_TYPE_INTERNAL_DICT = {
    MsgTypeInternal.CREATE_PLAYER: 'CREATE_PLAYER',
    MsgTypeInternal.DELETE_PLAYER: 'DELETE_PLAYER',
}


def get_enum_name(msg_type):
    if msg_type in MSG_TYPE_INTERNAL_DICT:
        return MSG_TYPE_INTERNAL_DICT[msg_type]
    return str(msg_type)

