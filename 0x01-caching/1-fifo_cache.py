#!/usr/bin/env python3
"""deifne a FIFOCLASS basecaching"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """class for fifo cacing"""
    def __init__(self):
        """the init method"""
        super().__init__()

    def put(self, key, item):
        """
        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in = next(iter(self.cache_data))
            self.cache_data.pop(first_in)
            print(f"DISCARD: {first_in}")

    def get(self, key):
        """
        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.cache_data.get(key, None)
