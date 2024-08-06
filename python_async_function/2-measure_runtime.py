#!/usr/bin/env python3
import asyncio
import time
from typing import List
wait_n = __import__('2-measure_runtime').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the average execution time of wait_n function """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))  # Run the wait_n function

    end_time = time.time()

    total_time = end_time - start_time  # Calculate total execution time

    return total_time / n  # Return average time per call
