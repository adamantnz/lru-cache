import pytest
from collections import OrderedDict
from lrucache import LRUCache
import itertools


class TestLRUCache:
    @pytest.fixture(autouse=False)
    def subject(self):
        """ create default class fixture """
        return LRUCache(capacity=1)

    @pytest.fixture(autouse=False)
    def default_lru_cache(self):
        """ create default lru cache fixture with two objects """
        context = LRUCache(capacity=5)
        context.set("1st key", "1st value")
        context.set("2nd key", "2nd value")
        return context

    def test_default_class_fixture_capacity_is_set(self, subject):
        """ test the default class fixture capacity instantiation """
        assert subject.capacity == 1

    def test_max_read_set(self, subject):
        """ test the max read cache constant is set """
        assert subject.max_number_cache_key_reads == 10

    @pytest.mark.parametrize("capacity", [-1, 0, None, -1000])
    def test_capacity_must_be_positive_exception(self, capacity):
        """ test a ValueError exception is raised when capacity is None or negative """
        with pytest.raises(ValueError):
            LRUCache(capacity=capacity)

    def test_keys_appended_to_lru_cache_exist(self, default_lru_cache):
        expected = OrderedDict([("1st key", "1st value"), ("2nd key", "2nd value")])
        assert default_lru_cache.cache == expected

    def test_keys_appended_to_lru_cache_are_in_correct_order_after_get(self):
        context = LRUCache(capacity=5)
        context.set("Michael", "Jordan")
        context.set("Scotty", "Pippen")
        context.get("Michael")
        expected = OrderedDict([("Scotty", "Pippen"), ("Michael", "Jordan")])
        assert context.cache == expected

    def test_key_is_removed_from_lru_cache_after_accessed_10_times(self):
        context = LRUCache(capacity=5)
        context.set("Michael", "Jordan")
        context.set("Scotty", "Pippen")
        for _ in range(11):
            context.get("Michael")
        expected = OrderedDict([("Scotty", "Pippen")])
        assert context.cache == expected
