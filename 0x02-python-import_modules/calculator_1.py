#!/usr/bin/python3

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)

def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)

def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

if __name__ == "__main__":
 print("{} + {} = {}".format(a, b, add(a, b)))
 print("{} - {} = {}".format(a, b, sub(a, b)))
 print("{} * {} = {}".format(a, b, mul(a, b)))
 print("{} / {} = {}".format(a, b, div(a, b)))
