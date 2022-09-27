#!/usr/bin/python3

"""
Defines a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a atext file (UTF8)

    Args:
        filename (str): name of the file to sppend the text to
        text (str): text to be appended

    Returns:
        The number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
