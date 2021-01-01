def substract(x, y):
    """Substract function"""
    return x-y


def add(x, y):
    """Add function"""
    return x+y


def divide(x, y):
    if y == 0:
        raise ValueError("Not divisible by zero")
    return x / y


def multiply(x, y):
    return x * y
