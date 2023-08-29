#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): Private attribute for the size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with the given size.
        area(self): Calculates and returns the current area of the square.
        size(self): Getter method to retrieve the value of size attribute.
        size(self, value): Setter method to set the value of size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.
        """
        self.size = size
        
    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    @property
    def size(self):
        """
        Getter method to retrieve the value of the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter method to set the value of the size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value
