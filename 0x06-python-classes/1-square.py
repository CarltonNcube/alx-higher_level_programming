#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): Private attribute for the size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
