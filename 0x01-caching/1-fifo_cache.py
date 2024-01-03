#!/usr/bin/python3

'''
A class representing a FIFO Cache.
'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    Initialize a new instance of the FIFOCache class.
    '''
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        Insert an item into the cache.
        If the cache is full, the least recently used item will be discarded.
        '''
        if key is None or item is None:
            return
        # Update the cache data
        self.cache_data[key] = item
        # Append the key to the order list
        self.order.append(key)
        # If cache exceeds its limit, remove the oldest item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            print("DISCARD:", oldest_key)
            del self.cache_data[oldest_key]

    def get(self, key):
        '''
        Retrieve an item from the cache.

        Parameters:
        key (str): The key for the item to be retrieved.

        Returns:
        object: The item retrieved from the cache.
                If the item does not exist in the cache,
                None is returned.
        '''
        return self.cache_data.get(key, None)
