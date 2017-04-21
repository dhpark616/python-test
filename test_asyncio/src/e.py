CREATE_PLAYER = 1
DELETE_PLAYER = 2

SERVER_MSG_TYPE = {
    CREATE_PLAYER: 'CREATE_PLAYER',
    DELETE_PLAYER: 'DELETE_PLAYER',
}


def get_enum_name(msg_type):
    if msg_type in SERVER_MSG_TYPE:
        return SERVER_MSG_TYPE[msg_type]
    return str(msg_type)

