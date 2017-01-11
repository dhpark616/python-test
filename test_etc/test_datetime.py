import datetime
from isoweek import Week  # pip install isoweek


def get_curr_year_week():
    check_time = datetime.datetime.now()
    return int('{}{:02d}'.format(check_time.isocalendar()[0], check_time.isocalendar()[1]))


def get_last_year_week():
    check_time = datetime.datetime.now() - datetime.timedelta(days=7)
    return int('{}{:02d}'.format(check_time.isocalendar()[0], check_time.isocalendar()[1]))


def main():
    print('{}, {}'.format(get_curr_year_week(), get_last_year_week()))
    '''
    d = "201326"
    r = datetime.datetime.strptime(d + '-1', "%Y%W")
    '''
    d = str(get_curr_year_week())
    r1 = datetime.datetime.strptime(d + '-1', "%Y%W-%w")
    r2 = datetime.datetime.strptime(d + '-0', "%Y%W-%w")
    print(r1.strftime('%Y-%m-%d'), r2.strftime('%Y-%m-%d'))

    d = str(get_last_year_week())
    r1 = datetime.datetime.strptime(d + '-1', "%Y%W-%w")
    r2 = datetime.datetime.strptime(d + '-0', "%Y%W-%w")
    print(r1.strftime('%Y-%m-%d'), r2.strftime('%Y-%m-%d'))

    r = Week(2016, 52).sunday()
    print(r)


if __name__ == '__main__':
    main()


