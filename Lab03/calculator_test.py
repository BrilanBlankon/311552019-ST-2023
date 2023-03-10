import unittest
from calculator import Calculator
from math import sqrt, exp


class ApplicationTest(unittest.TestCase):

    def test_add(self):
        # valid
        valid_list = [(1, 2, 3), (3, 4, 7), (5, 6, 11),
                      (7, 8, 15), (9, 10, 19)]
        for p1, p2, ans in valid_list:
            with self.subTest():
                self.assertEqual(Calculator.add(p1, p2), ans)
        # invalid
        invalid = ('a', True)
        self.assertRaises(TypeError, Calculator.add, invalid[0], invalid[1])

    def test_divide(self):
        # valid
        valid_list = [(1, 2, 0.5), (2, 1, 2.0), (5, 4, 1.25),
                      (4, 5, 0.8), (7, 8, 0.875)]
        for p1, p2, ans in valid_list:
            with self.subTest():
                self.assertEqual(Calculator.divide(p1, p2), ans)
        # invalid
        invalid = ('a', True)
        self.assertRaises(TypeError, Calculator.divide, invalid[0], invalid[1])

    def test_sqrt(self):
        # valid
        valid_list = [(4, sqrt(4)), (5, sqrt(5)), (9, sqrt(9)),
                      (16, sqrt(16)), (17, sqrt(17))]
        for p1, ans in valid_list:
            with self.subTest():
                self.assertEqual(Calculator.sqrt(p1), ans)
        # invalid
        invalid = 'a'
        self.assertRaises(TypeError, Calculator.sqrt, invalid)

    def test_exp(self):
        # valid
        valid_list = [(2, exp(2)), (3, exp(3)), (4, exp(4)),
                      (5, exp(5)), (6, exp(6))]
        for p1, ans in valid_list:
            with self.subTest():
                self.assertEqual(Calculator.exp(p1), ans)
        # invalid
        invalid = 'a'
        self.assertRaises(TypeError, Calculator.exp, invalid)


if __name__ == '__main__':
    unittest.main()
