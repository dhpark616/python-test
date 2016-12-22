import asyncio
import datetime


def get_datetime_str():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


def make_run_forever(func, period):
    async def task():
        while True:
            await asyncio.sleep(period)
            func()

    asyncio.ensure_future(task())
