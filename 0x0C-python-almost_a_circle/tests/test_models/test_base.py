#!/usr/bin/python3
"""
    Test base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
        Test cases for class
    """
    # test if input is None
    def test_None(self):
        B1 = Base()
        B2 = Base()
        B3 = Base(None)
        self.assertEqual(B1.id, 1)
        self.assertEqual(B2.id, 2)
        self.assertEqual(B3.id, 3)

    # test any input for id
    def test_input(self):
        b1 = Base(1)
        b2 = Base("str")
        b3 = Base([1, 3, 4])
        b4 = Base({1})
        b5 = Base(-1)
        b6 = Base(float("inf"))
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, "str")
        self.assertEqual(b3.id, [1, 3, 4])
        self.assertEqual(b4.id, {1})
        self.assertEqual(b5.id, -1)
        self.assertEqual(b6.id, float("inf"))
