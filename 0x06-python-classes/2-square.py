#!/usr/bin/python3
"""
Defines a square based on 1-square.py
"""


class Square:
    """
    Represnts a square object
    """

    def __init__(self, size=0):
        """
        Initialises a new sqaure object

        Args:
            size (int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
