""" lrucache.py """
from collections import OrderedDict
from contextlib import suppress


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cache_read_counter = OrderedDict()
        self.capacity = self._validate_capacity(capacity)

    def set(self, key: str, value: str) -> OrderedDict:
        """ parent method containing logic to add a key/value to the cache """
        self._pop_key(key)
        self._append_key(key, value)
        self._validate_capacity_exceeded()
        return self.cache

    def get(self, key: int) -> OrderedDict:
        """ parent method containing the logic to retrieve a given key from the cache """
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key, last=True)
            self._validate_key_is_valid(key)
        return self.cache

    def _validate_key_is_valid(self, key) -> None:
        """ private method to validate the cache key has not exceeded the maximum read count """
        try:
            item_accessed_count = self.cache_read_counter[key]
            self.cache_read_counter[key] = item_accessed_count + 1
            if self.cache_read_counter[key] >= self.max_number_cache_key_reads:
                self._pop_key(key)
                self.cache_read_counter[key] = 0
        except KeyError:
            # key is not in the read counter dict, so add it with a 0 counter
            self.cache_read_counter[key] = 0

    def _validate_capacity_exceeded(self) -> None:
        """ private method to maintain cache capacity """
        self.cache.popitem(last=False) if len(self.cache) > self.capacity else None

    def _append_key(self, key: str, value: str) -> None:
        """ private method to append a given key/value pair to the lru cache """
        self.cache[key] = value

    def _pop_key(self, key: str) -> None:
        """ private method to handle removing a given key from the lru cache """
        with suppress(KeyError):
            self.cache.pop(key)

    @staticmethod
    def _validate_capacity(capacity: int) -> int:
        """ private method to validate the capacity when class is instantiated """
        if isinstance(capacity, int) and capacity > 0:
            return capacity
        else:
            raise ValueError("capacity must be positive integer")

    @property
    def max_number_cache_key_reads(self):
        return 10
