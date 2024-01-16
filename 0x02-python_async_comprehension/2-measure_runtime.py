#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""


import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function return the total runtime for asynchronous comprehension
    running 4 times in parallel"""
    start_time = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
