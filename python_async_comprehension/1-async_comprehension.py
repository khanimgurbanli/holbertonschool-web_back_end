import random
import asyncio
from typing import List

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def async_comprehension() -> List[float]:
    """Asynchronous comprehension to collect random numbers"""
    return [value async for value in async_generator()]

# Example usage to see the output
if __name__ == "__main__":
    result = asyncio.run(async_comprehension())
    print(result)
