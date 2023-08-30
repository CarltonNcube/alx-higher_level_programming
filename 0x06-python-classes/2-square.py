#!/usr/bin/python3
"""A class that defines a square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

# Example usage:
if __name__ == "__main__":
    # Create a Square instance with size 5
    square = Square(5)
    print("Size:", square._Square__size)
    
    # Try to create a Square instance with a non-integer size
    try:
        invalid_square = Square("hello")
    except TypeError as e:
        print("Error:", e)
    
    # Try to create a Square instance with a negative size
    try:
        invalid_square = Square(-2)
    except ValueError as e:
        print("Error:", e)

