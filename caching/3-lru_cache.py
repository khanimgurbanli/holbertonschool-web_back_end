#!/usr/bin/python3
""" LRU Caching: Create a class LRUCache that inherits from BaseCaching
                 and is a caching system
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """An LRU Cache.
    Inherits all behaviors from BaseCaching except, upon any attempt to
    add an entry to the cache when it is at max capacity (as specified by
    BaseCaching.MAX_ITEMS), it discards the least recently used entry to
    accommodate for the new one.
    Attributes:
      __init__ - method that initializes class instance
      put - method that adds a key/value pair to cache
      get - method that retrieves a key/value pair from cache"""

    def __init__(self):
        """Initialize class instance."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add key-value pair to cache data.
        If cache is at max capacity BaseCaching.MAX_ITEMS,
        discard least recently used entry in cache to accommodate new
        entry"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {:s}".format(discard))

    def get(self, key):
        """Return value stored in key of cache
        If key is None or does not exist in cache. Return None"""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
