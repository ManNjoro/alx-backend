#!/usr/bin/env python3
"""
Implementation of an LRU Cache.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A simple class that provides caching functionality using the LRU strategy.
    The cache is implemented using an OrderedDict from the collections module,
    where the most recently accessed item is always at the end.
    When a new item is added, it is added at the beginning.
    If the cache is full and a new item is added,
    the least recently used item (the one at the end) is removed.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add a new item to the cache or update an existing item.
        If the key is None or the item is None, this method does nothing.
        If the key is not in the cache, it is added at the beginning.
        If the cache is full and a new item is added,
        the least recently used item is removed.
        If the key is already in the cache, its value is updated.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        If the key is not None and the key is in the cache,
        the item is moved to the end of the cache.
        If the key is not in the cache, None is returned.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
