# -*- coding: utf-8 -*-
"""Test file for insertion sort."""


# LIST_NUM_SORTED = range(10)
LIST_NUM_SORTED = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_NUM_SORTED2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_NUM_UNSORTED = [6, 2, 7, 1, 5, 3, 8, 4, 9, 0]
LIST_NUM_REVERSE = LIST_NUM_SORTED[::-1]


def test_best_case():
    from sort_insert import sort
    """Test best case sort. (pre-sorted)"""
    assert sort(LIST_NUM_SORTED2) == LIST_NUM_SORTED


def test_chaos_case():
    from sort_insert import sort
    """Test random case sort. (chaos sorted)"""
    assert sort(LIST_NUM_UNSORTED) == LIST_NUM_SORTED


def test_worse_case():
    from sort_insert import sort
    """Test worst case sort. (revrse-sorted)"""
    assert sort(LIST_NUM_REVERSE) == LIST_NUM_SORTED
