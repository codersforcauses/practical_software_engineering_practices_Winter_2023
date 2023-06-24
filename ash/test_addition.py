def hack(a, b):
    """hack a and b"""
    return a + b


def test_add():
    assert hack(1, 1) == 2
    assert hack(0, 0) == 0
    assert hack(1, -1) == 0
