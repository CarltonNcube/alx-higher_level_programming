#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): Private attribute for the size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

# Creating an instance of the Square class with size 3
my_square = Square(3)

# Printing the type and dictionary of the square object
print(type(my_square))
print(my_square.__dict__)

# Trying to access the size attribute directly
try:
    print(my_square.size)
except Exception as e:
    print(e)

# Trying to access the __size attribute directly
try:
    print(my_square.__size)
except Exception as e:
    print(e)
