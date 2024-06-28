#!/usr/bin/env python3
"""define a class for cache"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    defines a basic class for a basic cache
    """
    def put(self, key, item):
        """ puts item in cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ gets item from cache """
        return self.cache_data.get(key, None)
