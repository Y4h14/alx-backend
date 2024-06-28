#!/usr/bin/env python3
"""define a  mru cache class"""
BaseCaching = __import__("base_caching").BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """a class for MRU cache"""
    def __init__(self):
        """initalization method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru, _ = self.cache_data.popitem(False)
                print(f"DISCARD: {mru}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Args:
            key (_type_): _description_
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
