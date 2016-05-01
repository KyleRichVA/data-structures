#  -*- coding: utf-8 -*-
"""Test file for trie."""
import pytest
import io


TEST_DICT = {'t': {'e': {'s': {'t': {'$': {}, 'e': {'r': {'$': {}}}}}}}}


try:
    wordfile = io.open('src/test_strs.txt', encoding='utf8')
    WORDS = wordfile.readlines()
except:
    WORDS = []


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


@pytest.fixture()
def trie_ALL_THE_THINGS():
    from trie import Trie
    trie = Trie()
    for word in WORDS:
        trie.insert(word.strip('\n'))
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


def test_insert_non_string(trie_stuff):
    with pytest.raises(ValueError):
        trie_stuff.insert(42)


def test_insert_space_string(trie_empty):
    with pytest.raises(ValueError):
        trie_empty.insert('Hello Word')


def test_insert_cleans_string(trie_empty):
    trie_empty.insert('Hello$')
    assert trie_empty.contains('hello')


def test_traversal_empty(trie_empty):
    trav = trie_empty.traversal()
    lst = [word for word in trav]
    assert lst == []


def test_traversal_basic(trie_stuff):
    trav = trie_stuff.traversal()
    lst = [word for word in trav]
    assert 'test' in lst and 'tester' in lst


def test_traversal_after_insert(trie_stuff):
    trie_stuff.insert('bird')
    trav = trie_stuff.traversal()
    lst = [word for word in trav]
    assert 'test' in lst and 'tester' in lst and 'bird' in lst


def test_autocomplete_empty(trie_empty):
    assert trie_empty.autocomplete('test') == []


def test_autocomplete_basic(trie_stuff):
    result = trie_stuff.autocomplete('test')
    assert 'test' in result and 'tester' in result


# @pytest.mark.parametrize("word", WORDS)
# def test_ALL_THE_THINGS_CONTAINS(trie_ALL_THE_THINGS, word):
#     assert trie_ALL_THE_THINGS.contains(word.strip('\n').lower())


def test_ALL_THE_THINGS_TRAVERSAL(trie_ALL_THE_THINGS):
    trav = trie_ALL_THE_THINGS.traversal()
    lst = [word for word in trav]
    for word in WORDS:
        assert word.strip('\n').lower() in lst
