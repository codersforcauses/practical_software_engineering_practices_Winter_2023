def add(a, b):
    """Add a and b"""
    pass


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0

def divide(a,b):
    return a/b

def test_divide(a,b):
    assert divide(2,2) == 1
    assert divide(4,2) == 2
    assert divide(6,2) == 3