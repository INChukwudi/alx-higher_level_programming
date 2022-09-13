#!/usr/bin/python3
"""
Defines a square based on 4-square.py
"""


class Square:
    """
    Represents the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises a new sqaure object

        Args:
            size (int): size of the sqaure
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets and sets the value of the size attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute
        Validates the value to be set

        Args:
            value (int): new value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets and sets the value of the size attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute
        Validates the value to be set

        Args:
            value (tuple): new value of position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the sqaure object
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints in stdout the sqaure with the character #
        """
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
