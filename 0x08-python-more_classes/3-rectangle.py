#!/usr/bin/python3

"""
Defines a Rectangle class (based on 2-rectangle.py)
"""


class Rectangle:
    """
    Defines the structure of a Rectangle object
    """

    def __init__(self, width=0, height=0):
        """
        Initialises a new Reactangle instance

        Args:
            width (int): width of the rectangle instance
            height (int): height of the rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets and sets the width of the rectangle instance
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets the value of the width attribute
        Validates the value to be set is of type int
        Validates the value to be set is greater than 0

        Args:
            value (int): new value to assign to the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets and sets the height of the rectangle instance
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Sets the value of the height attribute
        Validates the value to be set is of type int
        Validates the value to be set is greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle instance area
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Returns the rectangle instance area
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance
        The rectangle instance is represented by the # character
        """
        if self.width == 0 or self.height == 0:
            return ("")

        string = []
        for i in range(self.height):
            for j in range(self.width):
                string.append("#")
            if i != self.height - 1:
                string.append("\n")
        return ("".join(string))
