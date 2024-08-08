#!/usr/bin/python3
""" Dictionary: Create a class BasicCache that inherits from BaseCaching
                      and is a caching system
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic cache.
    Inherits from class BaseCaching.
    Attributes:
      put - method that adds a key-value pair to cache
      get - method that retrieves a key-value pair from cache
    """


def put(self, key, item):
    """Add key-value pair to cache.
    If 'key' or 'item' is None, do nothing"""
    if key is not None or item is not None:
        self.cache_data[key] = item


def get(self, key):
    """Return value stored in 'key' of cache.
    If key is None or does not exist in cache, return None"""
    if key is not None and key in self.cache_data:
        return self.cache_data[key]
    return None
