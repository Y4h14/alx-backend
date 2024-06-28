#!/usr/bin/env python3
"""define a LIFO caching class"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """a class for a lifo cache"""
    def __init__(self):
        """initiaion method
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) > self.MAX_ITEMS:
                last_in = self.cache_data.popitem()
                print(f"DISCARD: {last_in[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """
        Args:
            key (_type_): _description_
        """
        return self.cache_data.get(key, None)
