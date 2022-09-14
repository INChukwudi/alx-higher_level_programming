#!/usr/bin/python3

"""
Defines a MagicClass that performs actions based on bytecode provided
"""

import math


class MagicClass:
    """
    Represents a MagicClass instance
    """

    def __init__(self, radius=0):
        """
        Inititalises a MagicClass instance

        Args:
            radius (int | float): radius of the MagicClass Instance
        """
        self.___radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the MagicClass instance
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Computes and returns the circumference of the MagicCLass instance
        """
        return (2 * math.pi * self.__radius)
