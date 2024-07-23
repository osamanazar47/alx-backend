#!/usr/bin/env python3
"""FIFOCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defining FIFOCache class"""
    def __init__(self):
        """initializing the class"""
        super().__init__()

    def put(self, key, item):
        """assigns a new pair to the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_in = next(iter(self.cache_data))
                print('DISCARD: {}'.format(first_in))
                del self.cache_data[first_in]

    def get(self, key):
        """returns the value of the given key from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
