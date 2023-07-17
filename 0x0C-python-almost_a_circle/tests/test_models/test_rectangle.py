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
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 4, 4, 18)

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

    # test correct output for area
    def test_area(self):
        self.assertEqual(self.r3.area(), self.r3.width * self.r3.height)
        self.assertEqual(self.r2.area(), self.r2.width * self.r2.height)
        self.assertEqual(self.r1.area(), self.r1.width * self.r1.height)
    # test update method
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(8)
        self.assertEqual(r1.id, 8)
        r1.update(89, 2, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        with self.assertRaises(TypeError):
            r1.update(89, 2, 2, '1')
            r1.update(89, 3, 4, '6')
            r1.update(89, [1], 3)
            r1.update(88, 2, 4, (1))
            r1.update(89, 2, 3, 5, {7})
        with self.assertRaises(ValueError):
            r1.update(89, -1)
            r1.update(89, 1, 0)
            r1.update(89, 1, 2, -1)
            r1.update(89, 3, 2, 1, -2)

    # test to dictionary
    def test_to_dictionary(self):
        s1 = Rectangle(10, 2, 1, 4, 3)
        self.assertEqual(s1.to_dictionary(), {'id': 3, 'width': 10,
                                              'height': 2, 'x': 1, 'y': 4})
