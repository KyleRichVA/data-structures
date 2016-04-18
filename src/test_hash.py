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


def test_set_collision(test_hash):
    test_hash.set(u'xz', 34)
    test_hash.set(u'yy', 25)
    # These two keys should have the same hash table index
    assert test_hash._table[2] == [(u'xz', 34), (u'yy', 25)]


def test_set_overwrite(test_hash):
    test_hash.set(KEY, 34)
    assert (KEY, 34) in test_hash._table[test_hash._hash(KEY)]
    test_hash.set(KEY, 100)
    assert (KEY, 34) not in test_hash._table[test_hash._hash(KEY)]
    assert (KEY, 100) in test_hash._table[test_hash._hash(KEY)]


def test_get_found(test_hash):
    test_hash.set(KEY, 34)
    assert test_hash.get(KEY) == 34


def test_get_not_there(test_hash):
    with pytest.raises(KeyError):
        test_hash.get(KEY)


@pytest.mark.parametrize("bads", BAD_ITEMS)
def test_get_non_string(test_hash, bads):
    with pytest.raises(TypeError):
        test_hash.get(bads)
