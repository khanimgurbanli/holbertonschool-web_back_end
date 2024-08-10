#!/usr/bin/python3
""" LFU Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Initialize class instance."""
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """Assign to the dictionary, LFU algorithm"""
        if key is not None and item is not None:
            if len(self.keys) == BaseCaching.MAX_ITEMS and key not in self.keys:
                discard = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[discard]
                del self.uses[discard]
                print("DISCARD: {:s}".format(discard))
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.uses[key] += 1

    def get(self, key):
        """Return the value linked"""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return self.cache_data[key]
        return None
