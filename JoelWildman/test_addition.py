def add(a, b):
    """Add a and b, but only sometimes"""
    return a + b - a + a*2 - b + b*2 - a


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0
