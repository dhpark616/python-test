import inspect
import random
import time
import types


# http://stackoverflow.com/questions/6527633/how-can-i-make-a-deepcopy-of-a-function-in-python
def copy_func(f, name=None):
    '''
    return a function with same code, globals, defaults, closure, and
    name (or provide a new name)
    '''
    fn = types.FunctionType(f.__code__, f.__globals__, name or f.__name__, f.__defaults__, f.__closure__)
    # in case f was given attrs (note this dict is a shallow copy):
    fn.__dict__.update(f.__dict__)
    return fn


def uuid64():
    base = int(time.time()) << 32
    rnd = random.SystemRandom().getrandbits(32)
    return base + rnd


def get_handler_uuid():
    stack_frame = inspect.stack()
    for frame in stack_frame:
        if 'func' in frame.frame.f_locals:
            func = frame.frame.f_locals['func']
            if hasattr(func, 'uuid'):
                return func.uuid
    return uuid64()


func_map = dict()


def msg_id(msg_id_):
    def func_wrapper(func):
        global func_map
        func.msg_id = msg_id_
        func_map[msg_id_] = func
        return func

    return func_wrapper


# 함수 복사 안한 버전
def get_func(msg_id_):
    if msg_id_ in func_map:
        func = func_map[msg_id_]
        func.uuid = uuid64()
        return func
    else:
        return None


# 함수 복사한 버전
def get_func_copy(msg_id_):
    if msg_id_ in func_map:
        func = copy_func(func_map[msg_id_])
        func.uuid = uuid64()
        return func
    else:
        return None


sign_up_req = 1
sign_in_req = 2


def give_item():
    print('give_item : {}'.format(get_handler_uuid()))


@msg_id(sign_up_req)
def h_sign_up_req():
    print('h_sign_up_req : {}'.format(get_handler_uuid()))
    give_item()


@msg_id(sign_in_req)
def h_sign_in_req():
    print('h_sign_in_req : {}'.format(get_handler_uuid()))
    give_item()


def main():
    print('-' * 80)
    func_list = list()
    for i in range(2):
        func = get_func(sign_up_req)
        func_list.append(func)
        func()

    for func in func_list:
        func()

    print('-' * 80)
    func_copy_list = list()
    for i in range(2):
        func = get_func_copy(sign_in_req)
        func_copy_list.append(func)
        func()

    for func in func_copy_list:
        func()
    print('-' * 80)


if __name__ == '__main__':
    main()
