#!/usr/bin/python3

"""
Defines a function that returns the JSON repsesntation of an object
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj (any): Python Object to convert to a JSON string
    """
    return json.dumps(my_obj)
