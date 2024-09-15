#!/usr/bin/env python3
""" redis module
"""

from functools import wraps

import redis
import requests

# Initialize Redis connection
r = redis.Redis()


def cache_result(expiration: int):
    """Decorator to cache the results of a function with expiration time"""

    def decorator(func):
        @wraps(func)
        def wrapper(url: str):
            # Check if result is in cache
            cached_result = r.get(f"cache:{url}")
            if cached_result:
                return cached_result.decode("utf-8")

            # Call the function and cache the result
            result = func(url)
            r.setex(f"cache:{url}", expiration, result)
            return result

        return wrapper

    return decorator


def track_access(func):
    """Decorator to track how many times a URL was accessed"""

    @wraps(func)
    def wrapper(url: str):
        # Increment the access count for the URL
        r.incr(f"count:{url}")
        return func(url)

    return wrapper


@cache_result(expiration=10)  # Cache for 10 seconds
@track_access
def get_page(url: str) -> str:
    """Fetches the HTML content of the given URL and returns it"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Test the function with a slow URL
    test_url = "http://slowwly.robertomurray.co.uk/"
    html_content = get_page(test_url)
    print(html_content)

    # Check the access count
    count = r.get(f"count:{test_url}")
    if count:
        print(f"URL {test_url} was accessed {int(count)} times")
