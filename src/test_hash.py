from hash_table import Hash_Table
import pytest

@pytest.fixture()
def test_hash():
    return Hash_Table(10)


def test_hash_init(test_hash):
    assert len(test_hash._table) == 10


def test_hash_hasher(test_hash):
    assert test_hash._hash('key') in range(len(test_hash._table))


def test_set_base(test_hash):
    pass