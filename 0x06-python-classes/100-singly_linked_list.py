#!/usr/bin/python3

"""
Defines classes for a singly linked list
"""


class Node:
    """
    Defines a mode of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initialises a node instance

        Args:
            data (int): data the node holds
            next_node (Node): reference to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Gets and sets the data attribute of the Node instance
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Sets the value of the data attribute
        Validates the value to be set

        Args:
            value (int): new value of the data attribute
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Gets and sets the value of the next_node attribute of the Node instance
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Sets the value of the next_node attribute
        valiates the value to be set

        Args:
            value (Node): reference to a Node object
        """
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a SinglyLinkedLIst instance
    """
    pass
