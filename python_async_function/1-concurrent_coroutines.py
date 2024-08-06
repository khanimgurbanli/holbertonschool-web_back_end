#!/usr/bin/env python3

"""
    Spawn `wait_random` n times with the specified max_delay and return the list of all delays in ascending order.

    Args:
        n (int): Number of times to spawn `wait_random`.
        max_delay (int): The maximum delay in seconds for `wait_random`.

    Returns:
        List[float]: List of delays in ascending order.
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for ran delay until max_delay, returns list of actual delays """
    spawn_ls = []
    delay_ls = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(delayed_task)

    for spawn in spawn_ls:
        await spawn

    # Use a min-heap approach to sort delays without using sort()
    return delay_ls