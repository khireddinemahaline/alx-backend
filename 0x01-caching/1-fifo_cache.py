#!/usr/bin/env python3
""" FIFO caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system
    """
    def __init__(self):
        """ Init
        """
        super().__init__()

    def put(self, key, item):
        """ Add item in the cash in order FIFO
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                key_to_del = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(key_to_del))
                del self.cache_data[key_to_del]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data and key:
            return self.cache_data[key]
        return None
