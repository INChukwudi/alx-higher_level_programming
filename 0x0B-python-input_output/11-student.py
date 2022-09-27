#!/usr/bin/python3

"""
Defines a class Student
"""


class Student:
    """
    Defines a Student object
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise a new student object instance

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Retrieves a dictionary representation of the Student instance

        Args:
            attr (list): list of attributes to retrieve
        """
        if (type(attr) == list and
                all(type(elem) == str for elem in attr)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json (dict): json holding attributes names and values
        """
        for k, v in json.items():
            setattr(self, k, v)
