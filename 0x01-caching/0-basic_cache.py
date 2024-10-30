#!/usr/bin/env python3
""" BasicCache defines:
      - caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - caching system
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        
    def get(self, key):
        if key in self.cache_data and key:
            return self.cache_data[key]
        return None
