# -*- coding: utf-8 -*-
"""Trie data structure."""


class Trie(object):

    def __init__(self):
        self._trie = {}

    def contains(self, token):
        cursor = self._trie
        for char in token:
            try:
                cursor = cursor[char]
            except KeyError:
                return False
        return '$' in cursor

    def insert(self, token):
        cursor = self._trie
        token += '$'
        for char in token:
            cursor = cursor.setdefault(char, {})
