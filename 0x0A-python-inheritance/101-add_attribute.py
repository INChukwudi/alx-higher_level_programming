#!/usr/bin/python3

"""
Defines a function that adds an attribute to an object
"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if possible

    Args:
        obj (any): object to add attribute to
        att (str): name of the attribute to add
        value (any): value of the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
