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

    p_triangle = [[1]]
    while len(p_triangle) != n:
        c_triangle = p_triangle[-1]
        tmp = [1]
        for i in range(len(c_triangle) - 1):
            tmp.append(c_triangle[i] + c_triangle[i + 1])
        tmp.append(1)
        p_triangle.append(tmp)
    return p_triangle
