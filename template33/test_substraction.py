def add(a, b):
    """Add a and b"""
    return a + b


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0

def subtraction(a, b):
    """Subtract a and b"""
    return a - b

def test_subtraction():
    assert subtraction(1, 1) == 0
    assert subtraction(0, 0) == 0
    assert subtraction(1, -1) == 2

    
