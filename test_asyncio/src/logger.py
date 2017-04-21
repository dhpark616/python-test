import logging
import logging.handlers
import os
import errno
from pythonjsonlogger import jsonlogger

from src.util.time_util import local_timetuple


# https://docs.python.org/3/library/logging.html#logrecord-attributes
RESERVED_ATTRS = (
    'args', 'asctime', 'created', 'exc_info', 'filename', 'funcName', 'levelname', 'levelno', 'lineno',
    'module', 'msecs', 'message', 'msg', 'name', 'pathname', 'process', 'processName', 'relativeCreated',
    'stack_info', 'thread', 'threadName', 'exc_text'
)


def merge_record_extra(record):
    for k, v in record.__dict__.items():
        if k not in RESERVED_ATTRS and not (hasattr(k, 'startswith') and k.startswith('_')):
            record.msg += ', {}[{}]'.format(k, v)


class StreamHandlerWithExtra(logging.StreamHandler):
    def emit(self, record):
        merge_record_extra(record)
        super().emit(record)


def init(name, config):
    log_level = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warn": logging.WARN,
        "warning": logging.WARN,
        "error": logging.ERROR,
    }

    format = '%(asctime)s,%(levelname)s,%(message)s,%(filename)s,%(funcName)s,%(lineno)s'
    formatter = jsonlogger.JsonFormatter(format)
    formatter.converter = local_timetuple
    path = os.path.normpath(config['path'])

    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    pathname = os.path.normpath(path + '/{}.json'.format(name))
    file_handler = logging.handlers.TimedRotatingFileHandler(
        pathname,
        when=config['rotation'],
        interval=1,
        encoding='utf-8',
        backupCount=config['backupCount'],
    )
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    if logger.hasHandlers():
        for old_handler in logger.handlers:
            logger.removeHandler(old_handler)
    logger.setLevel(log_level.get(config['level'], logging.INFO))
    logger.addHandler(file_handler)

    if config['use_stream_handler']:
        stream_handler = StreamHandlerWithExtra()
        formatter = logging.Formatter(format)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)


