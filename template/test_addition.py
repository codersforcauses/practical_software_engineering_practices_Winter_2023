def add(a, b):
    """Add a and b"""
    a+=b
    return a


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0
    assert add(3, 4) == 7
