class Hash_Table(object):

    def __init__(self, num_buckets):
        """Initiation Method of Hash Table.

        Length of Table is Based on Passed Value num_buckets."""
        self._table = [None] * num_buckets
