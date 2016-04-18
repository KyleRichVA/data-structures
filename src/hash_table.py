class Hash_Table(object):

    def __init__(self, num_buckets):
        """Initiation Method of Hash Table.

        Length of Table is Based on Passed Value num_buckets."""
        self._table = [[]] * num_buckets

    def _hash(self, key):
        """Return the index of the table based off the hashed key."""
        indx = 0
        for char in key:
            indx += ord(char)
        return indx % len(self._table)

    def set(self, key, val):
        """Set the value to key in the table."""
        try:
            indx = self._hash(key)
        except TypeError:
            raise TypeError(u"Must Use Strings For Keys")

        for tup in self._table[indx]:
            if tup[0] == key:
                tup_ind = self._table[indx].index(tup)
                self._table[indx][tup_ind] = (key, val)
                return
        self._table[indx].append((key, val))

    def get(self, key):
        """Get the value set to key in the table."""
        try:
            indx = self._hash(key)
        except TypeError:
            raise TypeError(u"Must Use Strings For Keys")

        for tup in self._table[indx]:
            if tup[0] == key:
                return tup[1]
        # Key wasn't found raise a key
        raise KeyError(u"Key Not Found in Hash Table")
