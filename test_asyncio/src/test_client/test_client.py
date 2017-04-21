import asyncio
import importlib
import logging
import signal

from . import client_network
from .. import logger


def cleanup():
    for client in client_network.CLIENTS:
        client._closing = True


def shutdown():
    for client in client_network.CLIENTS:
        if client._closing:
            continue
        client.loop.stop()


def add_signal_handler(loop):
    try:
        loop.add_signal_handler(signal.SIGINT, shutdown)
        loop.add_signal_handler(signal.SIGTERM, shutdown)
    except NotImplementedError:
        print('WARN : NotImplementedError -- add_signal_handler')


def configure():
    log_config = {
        "path": "/data/log",
        "level": "debug",
        "rotation": "H",
        "backupCount": 96,
        "use_stream_handler": True,
    }
    logger.init('test_client', log_config)
    importlib.import_module('.handlers', 'src.test_client')


def run(host, port, user_id, char_name):
    configure()

    loop = asyncio.get_event_loop()
    client_network.connect(loop, host, port, user_id, char_name)
    add_signal_handler(loop)

    try:
        print('test_client starting... host[{}], port[{}]'.format(host, port))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        for client in client_network.CLIENTS:
            client.close()
        loop.run_until_complete(cleanup())

    logging.info('test_client terminated')
    loop.close()
