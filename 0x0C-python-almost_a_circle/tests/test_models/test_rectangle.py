#!/usr/bin/python3
"""
    program for testing the rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        A class for testing the rectangle class
    """
    # test value <= 0 for height and width
    def test_less_than_or_equal_to_zero(self):
        with self.assertRaises(ValueError):
            w = Rectangle(-1, 2)
            h = Rectangle(4, -2)

    # test value < 0 for x and y
    def test_less_than_zero(self):
        with self.assertRaises(ValueError):
            xx = Rectangle(1, 4, -2, 4)
            yy = Rectangle(2, 3, 4, -2)

    # test if value is > 0 for height and width
    def test_value_greater_than_zero(self):
        w = Rectangle(2, 4)
        h = Rectangle(4, 2)
        self.assertGreater(w.width, 0)
        self.assertGreater(h.height, 0)

    # test if value is >= 0 for x  and y
    def test_value_greater_than_or_equal_to_zero(self):
        xx = Rectangle(2, 4, 0, 1)
        yy = Rectangle(2, 4, 1, 1)
        self.assertGreaterEqual(xx.x, 0)
        self.assertGreaterEqual(yy.y, 0)

    # test for type error
    def test_for_wrong_input_value(self):
        with self.assertRaises(TypeError):
            w = Rectangle("wrong value", 2)
            h = Rectangle(2, "wrong value")
            w_2 = Rectangle(None, 1)
            h_2 = Rectangle(1, None)
            w_3 = Rectangle([1, 2, 3], 3)
            h_3 = Rectangle(3, [1, 2, 3])
            xx = Rectangle(1, 2, "wrong value", 3)
            yy = Rectangle(1, 2, 3, "wrong value")
            xx_2 = Rectangle(1, 2, None, 4)
            yy_2 = Rectangle(1, 2, 4, None)
            xx_3 = Rectangle(1, 2, [1, 3, 3], 3)
            yy_3 = Rectangle(1, 2, 3, [1, 2, 3])

    # test for correct input value    
    def test_correct_input(self):
        w = Rectangle(2, 3)
        h = Rectangle(3, 3)
        xx = Rectangle(2, 3, 4, 5)
        yy = Rectangle(2, 3, 4, 5)
        self.assertEqual(w.width, 2)
        self.assertEqual(h.height, 3)
        self.assertEqual(xx.x, 4)
        self.assertEqual(yy.y, 5)

    def test_Base(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 4, 4, 18)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 18)

