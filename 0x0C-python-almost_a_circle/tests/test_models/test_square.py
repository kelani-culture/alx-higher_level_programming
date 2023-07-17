#!/usr/bin/python3
"""
    program for testing the square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        A class for testing the square class
    """
    def setUp(self):
        self.r1 = Square(10, 2)
        self.r2 = Square(2, 10)
        self.r3 = Square(10, 4, 4, 18)

    # test value <= 0 for size
    def test_less_than_or_equal_to_zero(self):
        with self.assertRaises(ValueError):
            w = Square(-1, 2)
            h = Square(4, -2)

    # test value < 0 for x and y
    def test_less_than_zero(self):
        with self.assertRaises(ValueError):
            xx = Square(1, -2, 4)
            yy = Square(2, 4, -2)

    # test for type error
    def test_for_wrong_input_value(self):
        with self.assertRaises(TypeError):
            w = Square("wrong value", 2)
            h = Square(2, "wrong value")
            w_2 = Square(None, 1)
            h_2 = Square(1, None)
            w_3 = Square([1, 2, 3], 3)
            h_3 = Square(3, [1, 2, 3])
            xx = Square(1, 2, "wrong value")
            yy = Square(1, 2, "wrong value")
            xx_2 = Square(1, 2, None)
            yy_2 = Square(1, 2, None)
            xx_3 = Square(1, 2, [1, 3, 3])
            yy_3 = Square(1, 2, [1, 2, 3])

    # test for correct input value    
    def test_correct_input(self):
        yy = Square(2, 3, 4)
        self.assertEqual(yy.size, 2)
        self.assertEqual(yy.x, 3)
        self.assertEqual(yy.y, 4)

    # test update method
    def test_update(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(8)
        self.assertEqual(r1.id, 8)
        r1.update(89, 2, 2)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 2)
        with self.assertRaises(TypeError):
            r1.update(89, 2, 2, '1')
            r1.update(89, 3, 4, '6')
            r1.update(89, [1], 3)
            r1.update(88, 2, 4, (1))
            r1.update(89, 2, 3, 5, {7})
        with self.assertRaises(ValueError):
            r1.update(89, -1)
            r1.update(89, 1, 2)
            r1.update(89, 3, 2, 1)

    # test to dictionary
    def test_to_dictionary(self):
        s1 = Square(16, 10, 2, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 16,
                                              'x': 10, 'y': 2})
        s2 = Square(20, 2, 1, 3)
        self.assertEqual(s2.to_dictionary(), {'id': 3, 'size': 20,
                                              'x': 2, 'y': 1})
