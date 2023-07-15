#!/usr/bin/python3
"""
    A program for testing the base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
        Test alll edge cases for the base class
    """
    def test_base(self):
        b_1 = Base()
        b_2 = Base(12)
        b_3 = Base()
        b_4 = Base(-2)
        b_5 = Base("I")
        self.assertEqual(b_1.id, 1)
        self.assertEqual(b_2.id, 12)
        self.assertEqual(b_3.id, 2)
        self.assertEqual(b_4.id, -2)
        self.assertEqual(b_5.id, "I")
