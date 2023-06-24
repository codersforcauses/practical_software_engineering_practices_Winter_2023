def add(a, b):
    """Add a and b"""
    pass


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0

def substraction(a, b):
    """Substract a and b"""
    return a - b

def test_substraction():
    assert substraction(1, 1) == 0
    assert substraction(0, 0) == 0
    assert substraction(1, -1) == 2

    
