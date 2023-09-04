#!/usr/bin/python3
"""A class that defines a square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square's area."""
        return self.__size ** 2
