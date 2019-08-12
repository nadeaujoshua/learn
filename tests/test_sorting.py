import random

import pytest

from learn.datastructures import LinkedList
from learn.sorting import (bubble_sort, _selection_sort, _selection_sort_alt,
                           _insertion_sort, _merge_sort)


def test_bubble_sort():
    l = LinkedList()
    l.add(3)
    l.add(100)
    l.add(0)
    l.add(1)
    bubble_sort(l)
    results = []
    node = l.head
    while node:
        results.append(node.value)
        node = node.next
    assert results == [0, 1, 3, 100]


def test__selection_sort():
    to_sort = [random.randint(-100, 100) for x in range(100)]
    check = sorted(to_sort)
    _selection_sort(to_sort)
    assert to_sort  == check


def test__selection_sort_alt():
    to_sort = [random.randint(-100, 100) for x in range(100)]
    check = sorted(to_sort)
    _selection_sort_alt(to_sort)
    assert to_sort  == check


def test__insertion_sort():
    to_sort = [random.randint(-100, 100) for x in range(100)]
    check = sorted(to_sort)
    _insertion_sort(to_sort)
    assert to_sort == check


def test__merge_sort():
    to_sort = [random.randint(-100, 100) for x in range(100)]
    check = sorted(to_sort)
    _merge_sort(to_sort)
    assert to_sort == check
