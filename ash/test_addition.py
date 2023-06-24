def add(x, y):
    """Adds x and y"""
    return x - y


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0
