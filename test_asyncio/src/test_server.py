import asyncio
import signal

from . import game_network

config = dict()
config['port'] = 21000

SERVER = None


def shutdown():
    if SERVER is not None:
        SERVER.close()
    asyncio.get_event_loop().stop()


def add_signal_handler():
    try:
        asyncio.get_event_loop().add_signal_handler(signal.SIGINT, shutdown)
        asyncio.get_event_loop().add_signal_handler(signal.SIGTERM, shutdown)
    except NotImplementedError:
        print('WARN : NotImplementedError -- add_signal_handler')


def run():
    add_signal_handler()

    coro = asyncio.get_event_loop().create_server(game_network.TCPServerConnection, port=config['port'])
    global SERVER
    SERVER = asyncio.get_event_loop().run_until_complete(coro)

    try:
        print('test_server starting... port[{}]'.format(config['port']))
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        shutdown()
