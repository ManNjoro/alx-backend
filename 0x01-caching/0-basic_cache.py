#!/usr/bin/python3
'''
This script contains the code for a caching system.

It provides the ability to store data in the cache using the 'put' method.
The 'get' method is used to retrieve the data from the cache using the key.

'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    A caching system.
    '''
    def put(self, key, item):
        '''
        Assigns to the dictionary self.cache_data
        the item value for the key key.

        If key or item is None, the function will not do anything.
        '''
        if key or item is None:
            pass
        self.cache_data.update({key: item})

    def get(self, key):
        '''
        Retrieves the data from the cache using the key.

        If key is None or key is not found in self.cache_data,
        the function will return None.

        param key: The key to use when searching for the item in the cache.
        return: The item found in the cache or None if not found.
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
