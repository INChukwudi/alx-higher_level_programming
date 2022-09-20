#!/usr/bin/python3

"""
Defines a function to print a sqaure
"""


def print_sqaure(size):
    """
    Prints a square with the character #

    Args:
        size (int): the width and height of the sqaure
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
