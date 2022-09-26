#!/usr/bin/python3

"""
Defines a function checks for inheritance
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance of a class

    Args:
        obj (any): object to check
        a_class (type): class to check against

    Returns:
        True - if obj is an inherited instance of a_class
        False - if obj is not
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
