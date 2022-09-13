#!/usr/bin/python3
"""
Defines a square based on 2-square.py
"""


class Square:
    """
    Represents the square
    """

    def __init__(self, size=0):
        """
        initialises a new sqaure object

        Args:
            size (int): size of the sqaure
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the sqaure object
        """
        return (self.__size * self.__size)
