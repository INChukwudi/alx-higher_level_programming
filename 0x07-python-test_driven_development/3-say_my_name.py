#!/usr/bin/python3

"""
Defines a function that prints out a name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name

    Args:
        first_name (str): user's first name
        last_name (str): user's last name
                        defaults to an empty string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
