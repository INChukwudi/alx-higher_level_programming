#!/usr/bin/python3

"""
Deines a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Defines MyInt Object
    Differs from an int as it inverts the == and =! oprations
    """

    def __eq__(self, value):
        """
        Behaves like the != operator
        """
        return self.real != value

    def __ne__(self, value):
        """
        Behaves like the == operator
        """
        return self.real == value
