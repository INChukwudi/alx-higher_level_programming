#!/usr/bin/python3

"""
Defines class Rectangle that inherites from BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle object
    """

    def __init__(self, width, height):
        """
        Initialises a new Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Computes and return the area of the rectangle instance
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the toString representation of the rectangle instance
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
