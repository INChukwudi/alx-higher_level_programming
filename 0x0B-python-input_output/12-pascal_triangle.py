#!/usr/bin/python3

"""
Defines a function that returna a Pascal Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of ints representing the Pascal's Triangle of n
    """
    if n <= 0:
        return []
