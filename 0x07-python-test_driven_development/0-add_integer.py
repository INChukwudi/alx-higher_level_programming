#!/usr/bin/python3

"""
Defines a functions that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Return the sum of the integer addition of a and b
    Floata are casted to ints

    Args:
        a (int | float): first digit
        b (int | float): second digit. Defaults to 98
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
