#!/usr/bin/python3

"""
Defines a Rectangle class (based on 8-rectangle.py)
"""


class Rectangle:
    """
    Defines the structure of a Rectangle object

    Attributes:
        number_of_instnces (int): number of Rectangle instances
        print_symbol (any): symbol used for the string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialises a new Rectangle instance
        Increments the number_of_instnces attribute

        Args:
            width (int): width of the rectangle instance
            height (int): height of the rectangle instance
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Reurns a new Rectangle instance with width == height == size

        Args:
            size (int): width and height of new Rectangle
        """
        return (cls(size, size))

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
                string.append(str(self.print_symbol))
            if i != self.height - 1:
                string.append("\n")
        return ("".join(string))

    def __repr__(self):
        """
        Return an 'offical' string representation of the rectangle instance
        """
        string = "Rectangle(" + str(self.width) + ", "
        string += str(self.height) + ")"
        return (string)

    def __del__(self):
        """
        Detects a rectangle instance deletion
        Prints out a message
        Decrements the number_of_instances attribute
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
