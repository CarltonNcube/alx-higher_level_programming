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

# Creating an instance of the Square class with size 3
my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

# Creating an instance of the Square class with default size
my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

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

# Trying to create a Square instance with a non-integer size
try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

# Trying to create a Square instance with a negative size
try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
