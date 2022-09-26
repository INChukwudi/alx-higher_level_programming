#!/usr/bin/python3

"""
Defines a class Sqaure that inherits feom class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a Square object
    """

    def __init__(self, size):
        """
        Initialises a Sqaure object instance

        Args:
            size (int): size of the Sqaure instance
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
