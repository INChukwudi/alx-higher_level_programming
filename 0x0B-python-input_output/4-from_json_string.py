#!/usr/bin/python3

"""
Defines a function that returns an object represnted by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str): JSON string to convert to a Python Object
    """
    return json.loads(my_str)
