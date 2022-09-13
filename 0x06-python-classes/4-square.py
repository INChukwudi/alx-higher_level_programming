#!/usr/bin/python3
"""
Defines a square based on 3-square.py
"""


class Square:
    """
    Represents the square
    """

    def __init__(self, size=0):
        """
        Initialises a new sqaure object

        Args:
            size (int): size of the sqaure
        """
        self.size = size

    @property
    def size(self):
        """
        Gets and sets the value of the size attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute
        Validates the value to be set

        Args:
            value (int): new value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the sqaure object
        """
        return (self.__size * self.__size)
