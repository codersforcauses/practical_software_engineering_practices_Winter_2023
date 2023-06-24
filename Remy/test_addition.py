def add(a, b):
    """Add a and b"""
    return a+b


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0
