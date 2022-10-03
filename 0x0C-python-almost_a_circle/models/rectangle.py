#!/usr/bin/python3

"""
Defines a Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle object
    Inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instanties a Rectangle object instance

        Args:
            width (int): width of the Rectangle instance
            height (int): height of the Rectangle instance
            x (int): x coordinate of the Rectangle instance
            y (int): y coordinate of the Rectangle instance
            if (int): identity number of the Rectangle instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets and sets the width attribute of the Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validates the value to be set for the width attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets and sets the height attribute of the Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validates the value to be set as the height attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets and sets the x coordinate of the Rectangle instance
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Validates the value to be set as the x coordinate of the Rectangle
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets and sets the y coordinate of the Rectangle instance
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Validates the value to be set as the y coordinate of the Rectangle
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectanlge instance
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance using the # charatcer
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Updates the Recatangle instance

        Args:
            *args (ints): attribute values
            **kwargs (dict): attributes key-value pairs
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle instance
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Returns the string representation of the Rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}\
                ".format(self.id, self.x, self.y, self.width, self.height)
