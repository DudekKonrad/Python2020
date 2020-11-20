import unittest
import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        result = "(" + str(self.x) + ", " + str(self.y) + ")"
        return result

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return Point(other.x * self.x, other.y * self.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):     # długość wektora
        result = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        return result


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(4, 3)

    def test_str(self):
        self.assertEqual(str(self.point), "(4, 3)")

    def test_repr(self):
        self.assertEqual(repr(self.point), "Point(4, 3)")

    def test_eq(self):
        self.assertTrue(self.point == Point(4, 3))
        self.assertFalse(self.point == Point(5, 5))

    def test_ne(self):
        self.assertTrue(self.point != Point(1, 1))
        self.assertFalse(self.point != Point(4, 3))

    def test_add(self):
        self.assertEqual(self.point + Point(2, 2), Point(6, 5))
        self.assertEqual(self.point + Point(-1, 2), Point(3, 5))
        self.assertEqual(self.point + Point(-1, -2), Point(3, 1))
        self.assertEqual(self.point + Point(1, -2), Point(5, 1))

    def test_sub(self):
        self.assertEqual(self.point-Point(2, 2), Point(2, 1))
        self.assertEqual(self.point-Point(-1, -1), Point(5, 4))
        self.assertEqual(self.point-Point(1, -5), Point(3, 8))
        self.assertEqual(self.point-Point(-7, 2), Point(11, 1))

    def test_mul(self):
        self.assertEqual(self.point * Point(2, 2), Point(8, 6))
        self.assertEqual(self.point * Point(-2, 2), Point(-8, 6))
        self.assertEqual(self.point * Point(2, -2), Point(8, -6))
        self.assertEqual(self.point * Point(-2, -2), Point(-8, -6))

    def test_length(self):
        self.assertEqual(self.point.length(), 5)

    def test_cross(self):
        self.assertEqual(self.point.cross(Point(2, 2)), 2)

    def tearDown(self):
        del self.point

if __name__ == '__main__':
    unittest.main()
