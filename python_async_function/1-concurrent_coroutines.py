#!/usr/bin/env python3

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `wait_random` n times with the specified max_delay and return the list of all delays in ascending order.

    Args:
        n (int): Number of times to spawn `wait_random`.
        max_delay (int): The maximum delay in seconds for `wait_random`.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]  # Create a list of tasks
    delays = await asyncio.gather(*tasks)  # Run all tasks concurrently and gather the results

    # Use a min-heap approach to sort delays without using sort()
    result = []
    while delays:
        min_value = min(delays)
        result.append(min_value)
        delays.remove(min_value)

    return result
