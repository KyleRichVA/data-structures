from hash_table import Hash_Table


def test_hash_init():
    test_hash = Hash_Table(25)
    assert len(test_hash._table) == 25