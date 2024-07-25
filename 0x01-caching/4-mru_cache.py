#!/usr/bin/env python3
"""Module for task 4."""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Defining the MRUCache class"""
    def __init__(self):
        """Initializing the class"""
        super().__init__()
        self.mru = {}
        self.tm = 0

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                newest_key = max(self.mru.keys(), key=lambda k: self.mru[k])
                print("DISCARD:", newest_key)
                self.cache_data.pop(newest_key)
                self.mru.pop(newest_key)
        self.cache_data[key] = item
        self.mru[key] = self.tm
        self.tm += 1

    def get(self, key):
        """Retrieves an element from the cache"""
        if key in self.cache_data:
            self.ru[key] = self.tm
            self.tm += 1
            return self.cache_data.get(key)
        return None
