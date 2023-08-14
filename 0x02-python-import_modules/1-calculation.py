#!/usr/bin/python3

def add(a, b):
    """Add two integers and return the result."""
    return a + b

def sub(a, b):
    """Subtract two integers and return the result."""
    return a - b

def mul(a, b):
    """Multiply two integers and return the result."""
    return a * b

def div(a, b):
    """Divide two integers and return the result."""
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")

