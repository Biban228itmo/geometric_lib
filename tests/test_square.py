import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        side = 1
        res = area(side)
        self.assertEqual(res,1)

    def test_perimeter(self):
        side = 1
        res = perimeter(side)
        self.assertEqual(res,4)

    def test_area_zero(self):
        side = 0
        res = area(side)
        self.assertEqual(res,0)

    def test_perimeter_zero(self):
        side = 0
        res = perimeter(side)
        self.assertEqual(res,0)

    def test_area_neg(self):
        side = -1
        res = area(side)
        self.assertRaises(AssertionError)

    def test_perimeter_neg(self):
        side = -1
        res = area(side)
        self.assertRaises(AssertionError)


if __name__ == '__main__':
    unittest.main()