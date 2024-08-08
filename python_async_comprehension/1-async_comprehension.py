#!/usr/bin/env python3
""" Details: Write a coroutine called async_generator that takes no
                 arguments.
                 The coroutine will loop 10 times, each time asynchronously
                 wait 1 second, then yield a random number between 0 and 10.
                 Use the random module.
"""

import random
import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> list[float]:
    """Return result"""
    return [value async for value in async_generator()]

