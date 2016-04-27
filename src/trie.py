# -*- coding: utf-8 -*-
"""Trie data structure."""


class Trie(object):

    def __init__(self):
        self._trie = {}

    def contains(self, token):
        """Return True/False if token is in the Trie."""
        cursor = self._trie
        for char in token:
            try:
                cursor = cursor[char]
            except KeyError:
                return False
        return '$' in cursor

    def insert(self, token):
        """Insert the token into the Trie."""
        cursor = self._trie
        token += '$'
        for char in token:
            cursor = cursor.setdefault(char, {})

    def traversal(self, start=None):
        """Generator which produces all the words in the Trie."""
        # Set the cursor either to the passed start or the head of the trie.
        path = [self._trie]
        words = ['']
        while path:
            cursor = path.pop()
            cur_word = words.pop()
            for char_key in list(cursor):
                if char_key == '$':
                    yield cur_word
                    continue
                path.append(cursor[char_key])
                words.append(cur_word+char_key)
