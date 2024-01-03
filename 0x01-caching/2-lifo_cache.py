#!/usr/bin/python3
'''
Implementation of a Last-In-First-Out (LIFO) cache
using the base caching class.

Features:
- Follows LIFO principle
- Provides basic caching operations like get and put.
- Keeps track of the order of insertion using a list.
- Adheres to the base caching class's constraint
    on the maximum number of items.
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    Implementation of a LIFO cache.
    '''
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        Insert an item into the cache.

        :param key: Key to store the item.
        :param item: Item to store.
        '''
        if key is None or item is None:
            return
        # Update the cache data
        self.cache_data[key] = item
        # Append the key to the order list
        self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            latest_key = self.order.pop()
            print("DISCARD:", latest_key)
            del self.cache_data[latest_key]

    def get(self, key):
        '''
        Retrieve an item from the cache.

        :param key: Key of the item to retrieve.
        :return: Item corresponding to the given key,
            or None if the key is not found.
        '''
        return self.cache_data.get(key, None)
