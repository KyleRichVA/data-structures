# -*- coding: utf-8 -*-
"""Trie data structure."""
import re
from past.builtins import basestring


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
        if not isinstance(token, basestring) or ' ' in token:
            raise ValueError('Token must be a one word string')
        token = re.sub(r'\W', '', token.lower())
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

    def autocomplete(self, token):
        """Returns a list of up to 4 possible words in the trie based off the token."""
        possibles = []
        traversal = self.traversal()
        for word in traversal:
            if token in word and len(possibles) < 4:
                possibles.append(word)
        return possibles
