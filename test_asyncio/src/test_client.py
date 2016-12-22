import asyncio
import signal

from . import game_network
from . import util

config = dict()
config['host'] = 'localhost'
config['port'] = 21000

CLIENT = None


def shutdown():
    if CLIENT is not None:
        CLIENT.close()
    asyncio.get_event_loop().stop()


def add_signal_handler():
    try:
        asyncio.get_event_loop().add_signal_handler(signal.SIGINT, shutdown)
        asyncio.get_event_loop().add_signal_handler(signal.SIGTERM, shutdown)
    except NotImplementedError:
        print('WARN : NotImplementedError -- add_signal_handler')


def run():
    add_signal_handler()

    coro = asyncio.get_event_loop().create_connection(lambda: game_network.TCPClientConnection(1001),
                                                      host=config['host'], port=config['port'])
    global CLIENT
    CLIENT = asyncio.get_event_loop().run_until_complete(coro)

    util.make_run_forever(game_network.send_hello, 3)

    try:
        print('test_client starting... host[{}] port[{}]'.format(config['host'], config['port']))
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        shutdown()
