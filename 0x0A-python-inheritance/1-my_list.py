#!/usr/bin/python3

"""
Defines a class MyList that inherits from list
"""


class MyList(list):
    """
    Prints the elements of the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
