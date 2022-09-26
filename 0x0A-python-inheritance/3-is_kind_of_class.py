#!/usr/bin/python3

"""
Defines a function that checks for the object instance
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance or inherited instance of a class

    Args:
        obj (any): the object to check
        a_class (type): the class to check against

    Returns:
        True - if obj is an instance or inherited instance of a_class
        False - if it is not
    """
    if isinstance(obj, a_class):
        return True
    return False
