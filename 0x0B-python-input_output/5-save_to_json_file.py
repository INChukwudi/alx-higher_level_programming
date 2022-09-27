#!/usr/bin/python3

"""
Defines a function that writes an Bject to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python Object to a text file using a JSON representation

    Args:
        my_obj (any): python object to write to file
        filename (str): name of the file to write the JSON representation
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
