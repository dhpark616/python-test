import datetime

_offset = None


def utc_timestamp(days=0, hours=0, minutes=0, seconds=0):
    utc = datetime.datetime.utcnow()
    utc += datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return int(utc.timestamp())


def offset():
    global _offset
    if _offset:
        return _offset
    offset_hours = 9
    offset_minutes = 0
    _offset = datetime.timedelta(hours=offset_hours, minutes=offset_minutes)
    return _offset


def timestamp_to_local_datetime(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp) + offset()


def str_to_datetime(datetime_str):
    return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def local_datetime(days=0, hours=0, minutes=0, seconds=0):
    return datetime.datetime.utcnow() + offset() + datetime.timedelta(days=days, hours=hours, minutes=minutes,
                                                                      seconds=seconds)


def local_str():
    return local_datetime().strftime('%Y-%m-%d %H:%M:%S.%f')


def local_timetuple():
    return local_datetime().timetuple()


