def add(a, b):
    """Add a and b"""
    return a+b


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, -1) == 0


def factorial(n):
    """Return n!"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
