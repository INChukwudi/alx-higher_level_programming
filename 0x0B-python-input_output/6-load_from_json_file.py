#!/usr/bin/python3

"""
Defines a function that creates an Object
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a `JSON file`

    Args:
        filename (str): name of the JSON file
    """
    with open(filename) as f:
        return json.load(f)
