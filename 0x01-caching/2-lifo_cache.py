#!/usr/bin/env python3
""" LIFO caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system
    """
    def __init__(self):
        """ Init
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add item in the cash in order LIFO
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                key_to_del = self.keys.pop()
                print("DISCARD: {}".format(key_to_del))
                del self.cache_data[key_to_del]
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data and key:
            return self.cache_data[key]
        return None
