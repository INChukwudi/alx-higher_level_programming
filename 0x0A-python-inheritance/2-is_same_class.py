#!/usr/bin/python3

"""
Defines a function to check the instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj (any): the object to check
        a_class (type): the class to check against

    Returns:
        True - if obj is exactly the instance of a_class
        False - if obj is not
    """
    if type(obj) == a_class:
        return True
    return False
