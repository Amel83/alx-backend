#!/usr/bin/python3
"""  main dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ to inherite from basecaching and is a caching system
        this is it, we are here """
    def put(self, key, item):
        """ dedicate the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ result value linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
