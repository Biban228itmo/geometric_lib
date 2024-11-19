import unittest
from calculate import calc
from math import pi


class TestCalculate(unittest.TestCase):
    def test_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = [1]
        res = calc(fig, func, size)
        self.assertEqual(res, pi)

    def test_square_area(self):
        fig = 'square'
        func = 'area'
        size = [1]
        res = calc(fig, func, size)
        self.assertEqual(res, 1)

    def test_triangle_area(self):
        fig = 'triangle'
        func = 'area'
        size = [5, 12, 13]
        res = calc(fig, func, size)
        self.assertEqual(res, 30)

    def test_circle_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [1]
        res = calc(fig, func, size)
        self.assertEqual(res, 2 * pi)

    def test_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [1]
        res = calc(fig, func, size)
        self.assertEqual(res, 4)

    def test_triangle_perimeter(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [5, 12, 13]
        res = calc(fig, func, size)
        self.assertEqual(res, 30)

    def test_wrong_fig(self):
        fig = 'rectangle'
        func = 'area'
        size = [1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_wrong_func(self):
        fig = 'circle'
        func = 'diagonal'
        size = [1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_wrong_size(self):
        fig = 'square'
        func = 'area'
        size = [1, 2]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_area_circle(self):
        fig = 'circle'
        func = 'area'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_area_square(self):
        fig = 'square'
        func = 'area'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_area_triangle(self):
        fig = 'triangle'
        func = 'area'
        size = [-5, -12, -13]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_perimeter_circle(self):
        fig = 'circle'
        func = 'perimeter'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_perimeter_square(self):
        fig = 'square'
        func = 'perimeter'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_perimeter_triangle(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [-5, -12, -13]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_wrong_size_triangle(self):
        fig = 'triangle'
        func = 'area'
        size = [1, 2, 10]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)


if __name__ == '__main__':
    unittest.main()