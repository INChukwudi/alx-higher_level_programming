#!/usr/bin/python3

"""
Defines a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file

    Args:
        filename (str): name of the file to write to
        text (str): text to write to the file

    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
