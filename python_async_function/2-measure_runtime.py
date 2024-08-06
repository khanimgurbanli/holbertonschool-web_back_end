#!/usr/bin/env python3
import asyncio
import time
from typing import List
wait_n = __import__('2-measure_runtime').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the average execution time of wait_n function
      Args:
            max_delay: max wait
            n: spawn function

        Return:
            float measure time
     """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time  # Calculate total execution time
