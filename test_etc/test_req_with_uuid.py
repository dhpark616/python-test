import inspect
import random
import time


def uuid64():
    base = int(time.time()) << 32
    rnd = random.SystemRandom().getrandbits(32)
    return base + rnd


def get_handler_uuid():
    stack_frame = inspect.stack()
    for frame in stack_frame:
        if 'func' in frame.frame.f_locals and 'parsed_req_with_uuid' in frame.frame.f_locals:
            req = frame.frame.f_locals['parsed_req_with_uuid']
            return req.uuid
    return uuid64()


func_map = dict()


def msg_id(msg_id_):
    def func_wrapper(func):
        global func_map
        func.msg_id = msg_id_
        func_map[msg_id_] = func
        return func

    return func_wrapper


def get_func(msg_id_):
    if msg_id_ in func_map:
        func = func_map[msg_id_]
        func.uuid = uuid64()
        return func
    else:
        return None


class ReqWithUUID:
    def __init__(self, obj):
        self.obj = obj
        self.uuid = uuid64()

    def __getattr__(self, item):
        return getattr(self.obj, item)


def parse_req(req):
    parsed_req = req
    parsed_req_with_uuid = ReqWithUUID(parsed_req)
    return parsed_req_with_uuid


sign_up_req = 1
sign_in_req = 2


def give_item():
    print('give_item : {}'.format(get_handler_uuid()))


@msg_id(sign_up_req)
def h_sign_up_req(req):
    print('h_sign_up_req : {}'.format(get_handler_uuid()))
    give_item()


@msg_id(sign_in_req)
def h_sign_in_req(req):
    print('h_sign_in_req : {}'.format(get_handler_uuid()))
    give_item()


def main():
    req = {}

    print('-' * 80)
    func_list = list()
    parsed_req_with_uuid_list = list()
    for i in range(2):
        func = get_func(sign_up_req)
        func_list.append(func)
        parsed_req_with_uuid = parse_req(req)
        parsed_req_with_uuid_list.append(parsed_req_with_uuid)
        func(parsed_req_with_uuid)

    for func, parsed_req_with_uuid in zip(func_list, parsed_req_with_uuid_list):
        func(parsed_req_with_uuid)

    print('-' * 80)


if __name__ == '__main__':
    main()
