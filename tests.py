from partition.partition import partition


def array_equal(this, that):

    for a, b in zip(this, that):
        if a != b:
            return False

    return True

def test_partition():
    s = 6
    bound = (5, 4)

    expect = [(2, 4), (3, 3), (4, 2), (5, 1)]
    actual = partition(s, bound)
    for tuple_a, tuple_b in zip(actual, expect):
        array_equal(tuple_a, tuple_b)
