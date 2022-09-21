#!/usr/bin/python3

"""
Defines a class with no class or object attribute
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance atrributes
    Only creat an intance attribute if the attrivute is first_name
    """
    __slots__ = ["first_name"]
