#!/usr/bin/python3
""" LFU Caching """
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        super().__init__()
        self.lru_cache = OrderedDict()
        self.lfu_cache = {}

    def put(self, key, item):
        """Assign to the dictionary, LFU algorithm"""
        if key is None or item is None:
            return

        if key in self.lru_cache:
            del self.lru_cache[key]

        if len(self.lru_cache) >= BaseCaching.MAX_ITEMS:
            # Find the least frequently used item
            min_value = min(self.lfu_cache.values(), default=0)
            lfu_keys = [k for k, v in self.lfu_cache.items() if v == min_value]

            if len(lfu_keys) == 1:
                discard_key = lfu_keys[0]
            else:
                # If multiple items have the same frequency, discard the least recently used
                discard_key = next(k for k in self.lru_cache if k in lfu_keys)

            print("DISCARD:", discard_key)
            self.lru_cache.pop(discard_key)
            del self.lfu_cache[discard_key]

        self.lru_cache[key] = item
        self.lru_cache.move_to_end(key)

        # Update frequency
        if key in self.lfu_cache:
            self.lfu_cache[key] += 1
        else:
            self.lfu_cache[key] = 1

        self.cache_data = dict(self.lru_cache)

    def get(self, key):
        """Return the value linked"""
        if key in self.lru_cache:
            value = self.lru_cache[key]
            self.lru_cache.move_to_end(key)
            if key in self.lfu_cache:
                self.lfu_cache[key] += 1
            else:
                self.lfu_cache[key] = 1
            return value
