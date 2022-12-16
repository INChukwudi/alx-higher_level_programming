#!/usr/bin/python3
"""
Defines a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers
    """

    if list_of_integers == []:
        return None

    count = len(list_of_integers)
    if count == 1:
        return list_of_integers[0]
    if count == 2:
        return max(list_of_integers)

    mid = int(count / 2)
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
