#!/usr/bin/env python3
'''task 0'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for another random number'''
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
