import datetime

OFFSET_HOUR = 9
OFFSET_MINUTE = 0


def offset():
    offset_hour = OFFSET_HOUR
    offset_minute = OFFSET_MINUTE
    return datetime.timedelta(hours=offset_hour, minutes=offset_minute)


def local_datetime(days=0, hours=0, minutes=0):
    return datetime.datetime.utcnow() + offset() + datetime.timedelta(days=days, hours=hours, minutes=minutes)


def get_year_week(datetime_str, reset_day=1, reset_hour=0):
    delta_day = -6 if reset_day == 0 else 1 - reset_day
    dt = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    check_time = dt + datetime.timedelta(days=delta_day, hours=-reset_hour)
    return int('{}{:02d}'.format(check_time.isocalendar()[0], check_time.isocalendar()[1]))


def get_curr_year_week(reset_day=1, reset_hour=0):
    delta_day = -6 if reset_day == 0 else 1 - reset_day
    check_time = local_datetime(days=delta_day, hours=-reset_hour)
    return int('{}{:02d}'.format(check_time.isocalendar()[0], check_time.isocalendar()[1]))


def get_last_year_week(reset_day=1, reset_hour=0):
    delta_day = -6 if reset_day == 0 else 1 - reset_day
    check_time = local_datetime(days=delta_day, hours=-reset_hour) - datetime.timedelta(days=7)
    return int('{}{:02d}'.format(check_time.isocalendar()[0], check_time.isocalendar()[1]))


def get_next_year_week(reset_day=1, reset_hour=0):
    delta_day = -6 if reset_day == 0 else 1 - reset_day
    check_time = local_datetime(days=delta_day, hours=-reset_hour) + datetime.timedelta(days=7)
    return int('{}{:02d}'.format(check_time.isocalendar()[0], check_time.isocalendar()[1]))


def main():
    print('{}, {}, {}'.format(get_last_year_week(), get_curr_year_week(), get_next_year_week()))

    d = str(get_last_year_week())
    r1 = datetime.datetime.strptime(d + '-1', "%Y%W-%w")
    r2 = datetime.datetime.strptime(d + '-0', "%Y%W-%w")
    print('get_last_year_week() =', r1.strftime('%Y-%m-%d'), r2.strftime('%Y-%m-%d'))

    d = str(get_curr_year_week())
    r1 = datetime.datetime.strptime(d + '-1', "%Y%W-%w")
    r2 = datetime.datetime.strptime(d + '-0', "%Y%W-%w")
    print('get_curr_year_week() =', r1.strftime('%Y-%m-%d'), r2.strftime('%Y-%m-%d'))

    d = str(get_next_year_week())
    r1 = datetime.datetime.strptime(d + '-1', "%Y%W-%w")
    r2 = datetime.datetime.strptime(d + '-0', "%Y%W-%w")
    print('get_next_year_week() =', r1.strftime('%Y-%m-%d'), r2.strftime('%Y-%m-%d'))

    base_datetime_str = '2017-03-20 03:59'
    for i in range(7):
        print(get_year_week(base_datetime_str, i, 4))

    base_datetime_str = '2017-03-20 04:00'
    for i in range(7):
        print(get_year_week(base_datetime_str, i, 4))

if __name__ == '__main__':
    main()


