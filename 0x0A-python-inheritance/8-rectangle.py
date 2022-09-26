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
