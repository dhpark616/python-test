import asyncio
import importlib
import logging
import os
import signal
import sys

import cfg
from . import server_network
from .. import logger

SERVER = None


def cleanup():
    SERVER._closing = True


def shutdown():
    if SERVER._closing:
        return
    SERVER.loop.stop()


def add_signal_handler(loop):
    try:
        loop.add_signal_handler(signal.SIGINT, shutdown)
        loop.add_signal_handler(signal.SIGTERM, shutdown)
    except NotImplementedError:
        print('WARN : NotImplementedError -- add_signal_handler')


def configure(phase):
    cfg.load(phase)
    logger.init('ch_server', cfg.config['log'])
    importlib.import_module('.handlers', 'src.ch_server')


def run(phase):
    configure(phase)

    port = cfg.config['ch']['port']
    is_reuse_port = os.name == 'posix' and sys.platform != 'cygwin'
    loop = asyncio.get_event_loop()
    coro = loop.create_server(server_network.TCPServerConnection, port=port, reuse_address=True,
                              reuse_port=is_reuse_port)
    global SERVER
    SERVER = loop.run_until_complete(coro)
    SERVER.loop = loop
    SERVER._closing = False
    add_signal_handler(loop)

    try:
        print('ch_server starting... port[{}]'.format(port))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        SERVER.close()
        loop.run_until_complete(cleanup())

    logging.info('ch_server terminated')
    loop.close()
