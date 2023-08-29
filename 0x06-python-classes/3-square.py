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
        self.__size = size

        # Checking if the provided size is valid
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

# Creating an instance of the Square class with size 3
my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

# Trying to access the size attribute directly
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

# Trying to access the __size attribute directly
try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

# Creating an instance of the Square class with size 5
my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

