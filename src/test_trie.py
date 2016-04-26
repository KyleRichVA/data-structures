#  -*- coding: utf-8 -*-
"""Test file for trie."""
import pytest


TEST_DICT = {'t': {'e': {'s': {'t': {'$': {}, 'e': {'r': {'$': {}}}}}}}}


@pytest.fixture()
def trie_empty():
    from trie import Trie
    return Trie()


@pytest.fixture()
def trie_stuff():
    from trie import Trie
    trie = Trie()
    trie._trie = TEST_DICT
    return trie


def test_contains_empty(trie_empty):
    assert not trie_empty.contains("test")


def test_contains_test(trie_stuff):
    assert trie_stuff.contains("test")


def test_contains_tester(trie_stuff):
    assert trie_stuff.contains("tester")


def test_contains_not_toast(trie_stuff):
    assert not trie_stuff.contains("toast")


def test_insert_empty(trie_empty):
    trie_empty.insert("test")
    assert trie_empty.contains("test")


def test_insert_test(trie_stuff):
    """
    Assert attempting to insert word already present does not throw an error.
    Due to using dictionaries & setdefault, values cannot be overwritten.
    """
    trie_stuff.insert("test")
    assert trie_stuff.contains("test")
    assert trie_stuff.contains("tester")


def test_insert_tests(trie_stuff):
    trie_stuff.insert("tests")
    assert trie_stuff.contains("tests")


def test_insert_bird(trie_stuff):
    trie_stuff.insert("bird")
    assert trie_stuff.contains("bird")
