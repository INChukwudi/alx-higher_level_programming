#!/usr/bin/python3

"""
Defines a function that insertes text in a file after a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserta a line of text to a file after each line containing search_string

    Args:
        filename (str): name of the file
        search_string (str): string to search for within the file
        new_string (str): string to insert
    """
    text = ""
    with open(filename) as rf:
        for line in rf:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wf:
        wf.write(text)
