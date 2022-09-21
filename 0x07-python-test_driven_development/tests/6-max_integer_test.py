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
         self.assertEqual(max_integer(test_list), 4)
