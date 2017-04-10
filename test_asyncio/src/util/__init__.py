import asyncio


def make_run_forever(func, period):
    async def task():
        while True:
            await asyncio.sleep(period)
            func()

    asyncio.ensure_future(task())
