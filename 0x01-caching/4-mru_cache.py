#!/usr/bin/env python3
"""
Most Recently Used (MRU) Cache Implementation
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Most Recently Used (MRU) Cache Implementation
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.

        If the key already exists, it updates the value.
        If the key does not exist and the cache is full,
        it discards the oldest element to make space
        for the new key-value pair.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a value from the cache using a key.

        Args:
            key (hashable): The key to use to retrieve the value.

        Returns:
            value: The value associated with the key if it exists,
                    None otherwise.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
