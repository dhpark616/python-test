import logging
import logging.handlers
import time
import random
import os
import errno
import datetime

from pythonjsonlogger import jsonlogger

_offset = None


def offset():
    global _offset
    if _offset:
        return _offset
    offset_hours = 9
    offset_minutes = 0
    _offset = datetime.timedelta(hours=offset_hours, minutes=offset_minutes)
    return _offset


def local_datetime(days=0, hours=0, minutes=0, seconds=0):
    return datetime.datetime.utcnow() + offset() + datetime.timedelta(days=days, hours=hours, minutes=minutes,
                                                                      seconds=seconds)


def local_timetuple(_=None):
    return local_datetime().timetuple()


def init_log(name):
    log_level = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warn": logging.WARN,
        "warning": logging.WARN,
        "error": logging.ERROR,
    }

    config = dict()
    config['log'] = {
        "path": "/data/log",
        "level": "debug",
        "rotation": "H",
        "backupCount": 96,
    }

    format = '%(asctime)s,%(levelname)s,%(message)s,%(filename)s,%(funcName)s,%(lineno)s'
    formatter = jsonlogger.JsonFormatter(format)
    formatter.converter = local_timetuple
    path = os.path.normpath(config['log']['path'])

    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    pathname = os.path.normpath(path + '/{}.json'.format(name))
    file_handler = logging.handlers.TimedRotatingFileHandler(
        pathname,
        when=config['log']['rotation'],
        interval=1,
        encoding='utf-8',
        backupCount=config['log']['backupCount'],
    )
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    if logger.hasHandlers():
        for old_handler in logger.handlers:
            logger.removeHandler(old_handler)
    logger.setLevel(log_level.get(config['log']['level'], logging.INFO))
    logger.addHandler(file_handler)


def main():
    init_log('test_log')

    msg_type_list = ['enter_dungeon_req', 'start_dungeon_req', 'clear_dungeon_req', 'get_guild_list_req']
    req_list = [
        {"char_id": 6374631416888714762, "dungeon_mid": 113233},
        {"char_id": 6403280809782143819, "dungeon_mid": 113222},
        {"char_id": 6379059904668315720, "dungeon_mid": 113226},
        {"char_id": 6386401102156267233, "dungeon_mid": 113312},
    ]
    err_code_list = ['err_none', 'err_server_not_found_character', 'err_server_invalid_dungeon_mid',
                     'err_server_not_friend']
    ack_list = [
        {"err_code": 10001, "dungeon_mid": 113233},
        {"err_code": 10002, "dungeon_mid": 113222},
        {"err_code": 10003, "dungeon_mid": 113226},
        {"err_code": 10004, "dungeon_mid": 113312},
    ]

    for i in range(1000):
        time.sleep(1)
        if random.randint(1, 100) > 90:
            try:
                a = 100 / 0
            except Exception as e:
                logging.exception(e)
        else:
            logging.info("packet", extra={
                "msg_type": random.choice(msg_type_list),
                "req": random.choice(req_list),
                "err_code": random.choice(err_code_list),
                "ack": random.choice(ack_list),
                "latency": random.randint(1, 99999) / 10000,
            })


if __name__ == '__main__':
    main()
