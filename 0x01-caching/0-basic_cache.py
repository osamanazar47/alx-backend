#!/usr/bin/env python3
"""BasicCache Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defining BasicCache class"""
    def __init__(self):
        """Initializing the class"""
        super().__init__()

    def put(self, key, item):
        """Assign key- value pair in the caching data"""
        if key and item:
            self.cache_data[key] = item
        else:
            return

    def get(self, key):
        """returns the value of the given key from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
