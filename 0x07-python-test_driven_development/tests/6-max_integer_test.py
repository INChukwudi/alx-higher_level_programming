#!/usr/bin/python3

"""
Unittests for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines tests for the max_integer function
    """

    def test_ordered_list(self):
        """
        Test for an ordered list of ints
        """
        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)
