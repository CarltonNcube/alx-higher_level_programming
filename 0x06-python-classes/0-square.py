#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        side_length (float): The length of all sides of the square.

    Methods:
        __init__(self, side_length): Initializes a new Square instance with the given side length.
        area(self): Calculates the area of the square.
        perimeter(self): Calculates the perimeter of the square.
    """

    def __init__(self, side_length):
        """
        Initializes a new Square instance.

        Args:
            side_length (float): The length of all sides of the square.
        """
        self.side_length = side_length

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.side_length ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        return 4 * self.side_length

