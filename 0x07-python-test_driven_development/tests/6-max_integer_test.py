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
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(test_list), 5)

    def test_unordered_list(self):
        """
        Test an unordered list of ints
        """
        test_list = [1, 5, 2, 4, 3]
        self.assertEqual(max_integer(test_list), 5)

    def test_max_at_the_start(self):
        """
        Test a list with the max value at the start of the list
        """
        test_list = [5, 4, 3, 2, 1, 0]
        self.assertEqual(max_integer(test_list), 5)

    def test_empty_line(self):
        """
        Test an empty list
        """
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_single_element_list(self):
        """
        Test a list with a single element
        """
        test_list = [9]
        self.assertEqual(max_integer(test_list), 9)

    def test_ints_and_floats(self):
        """
        Test a list with ints and floats as its elements
        """
        test_list = [1.5, 2, 3.4, 5, 6.7]
        self.assertEqual(max_integer(test_list), 6.7)
