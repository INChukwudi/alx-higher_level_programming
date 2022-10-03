#!/usr/bin/python3

"""
Defines a Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Square object
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialises a new Sqaure object instance

        Args:
            size (int): size of the Square instance
            x (int): x coordinate of the Square instance
            y (int): y coordinate of the Square instance
            id (int): identity number of the Sqaure instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets and sets the size attribute of the Square instance
        """
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Sqaure instance

        Args:
            *args (ints): attibutes values
            **kwargs (dict): attibutes key-value pairs
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size == val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Squre instance
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the string representation of the Square instance
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)
