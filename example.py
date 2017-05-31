#!/usr/bin/env python3


# Requires Python 3.5+


import asyncio
import asyncioplus
from itertools import islice

async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1.0 / number)
    print("Finishing %d" % number)
    return str(number)

async def print_when_done(tasks):
    for res in asyncioplus.limited_as_completed(tasks, 10):
        print("Result %s" % await res)
coros = (mycoro(i) for i in range(1, 101))
loop = asyncio.get_event_loop()
loop.run_until_complete(print_when_done(coros))
loop.close()
