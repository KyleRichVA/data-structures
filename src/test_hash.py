from hash_table import Hash_Table
import pytest

KEY = u'key'
BAD_ITEMS = [1, True, {'Bad': 'Bad'}, ['bad', 13]]


@pytest.fixture()
def test_hash():
    return Hash_Table(10)


def test_hash_init(test_hash):
    assert len(test_hash._table) == 10


def test_hash_hasher(test_hash):
    assert test_hash._hash(KEY) in range(len(test_hash._table))


def test_set_base(test_hash):
    test_hash.set(KEY, 34)
    ind = test_hash._hash(KEY)
    assert (KEY, 34) in test_hash._table[ind]


@pytest.mark.parametrize("bads", BAD_ITEMS)
def test_set_non_string(test_hash, bads):
    with pytest.raises(TypeError):
        test_hash.set(bads, 34)