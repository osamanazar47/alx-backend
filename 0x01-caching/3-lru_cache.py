#!/usr/bin/env python3
"""Module for task 3."""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Defining the LRUCache class"""
    def __init__(self):
        """Initializing the class"""
        super().__init__()
        self.lru = {}
        self.tm = 0

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            print("DISCARD:", old_key)
            self.cache_data.pop(old_key)
            self.lru.pop(old_key)
        self.cache_data[key] = item
        self.lru[key] = self.tm
        self.tm += 1

    def get(self, key):
        """Retrieves an element from the cache"""
        if key in self.cache_data:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache_data.get(key)
        return None
