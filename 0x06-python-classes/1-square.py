#!/usr/bin/python3

"""A class that defines a square."""

class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square instance with the given size."""
        self.__size = size

# Example usage:
if __name__ == "__main__":
    # Create a Square instance with size 5
    square = Square(5)
    # Access the private attribute using the name mangling syntax
    print("Size:", square._Square__size)
