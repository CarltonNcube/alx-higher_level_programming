#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): Private attribute for the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.
        """
        # Checking if the provided size is valid
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
