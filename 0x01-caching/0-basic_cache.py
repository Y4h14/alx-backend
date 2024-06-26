#!/usr/bin/env python3
"""define a class for cache"""
BaseCaching = __import__('BaseCaching').BaseCaching


class BasicCache(BaseCaching):
    """
    defines a basic class for a basic cache
    """
    def put(self, key, item):
        """_summary_

        Args:
            key (str): cache item key
            item (Any): item stored in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """

        Args:
            key (str): the cache item key
        """
        return self.cache_data.get(key, None)
