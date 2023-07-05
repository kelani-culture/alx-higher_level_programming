#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Testing......................................
    """
    def test_max_end(self):
        self.assertEqual(max_integer([4, 3, 5, 6, 2, 10]), 10)

    def test_max_begin(self):
        self.assertEqual(max_integer([10, 2, 3, 4, 9, 0]), 10)

    def test_max_middle(self):
        self.assertEqual(max_integer([3, 1, 1, 5, 0, 3, 4]), 5)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -4, -4, -5]), -1)

    def test_oneNegative(self):
        self.assertEqual(max_integer([10, 4, -1, 3, 11]), 11)

    def test_oneElement(self):
        self.assertEqual(max_integer([3]), 3)

    def test_EmptyList(self):
        self.assertEqual(max_integer([]), None)
