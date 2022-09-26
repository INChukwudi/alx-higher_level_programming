#!/usr/bin/python3

"""
Defines the BaseGeometry class based on 6-base_geometry.py
"""


class BaseGeometry:
    """
    Defines the BaseGeometry instance
    """

    def area(self):
        """
        Method to compute the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer

        Args:
            name (str): name of the paramter passed
            value (int): parameter passed
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
