from points import Point
import unittest
import math


class Rectangle:
	"""Klasa reprezentująca prostokąt na płaszczyźnie."""

	def __init__(self, x1, y1, x2, y2):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self):  # "[(x1, y1), (x2, y2)]"
		return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(
			self.pt2.y) + ")]"

	def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
		return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
			self.pt2.y) + ")"

	def __eq__(self, other):  # obsługa rect1 == rect2
		return self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and \
		       self.pt2.y == other.pt2.y

	def __ne__(self, other):  # obsługa rect1 != rect2
		return not self == other

	def center(self):  # zwraca środek prostokąta
		return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

	def area(self):  # pole powierzchni
		return math.pow(self.pt2.x - self.pt1.x, 2) + math.pow(self.pt2.y - self.pt1.y, 2)

	def move(self, x, y):  # przesunięcie o (x, y)
		return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)


class TestRectangle(unittest.TestCase):

	def setUp(self):
		self.rectangle = Rectangle(0, 0, 4, 3)

	def test_str(self):
		self.assertEqual(str(self.rectangle), "[(0, 0), (4, 3)]")

	def test_repr(self):
		self.assertEqual(repr(self.rectangle), "Rectangle(0, 0, 4, 3)")

	def test_eq(self):
		self.assertTrue(self.rectangle == Rectangle(0, 0, 4, 3))
		self.assertFalse(self.rectangle == Rectangle(1, 2, 4, 3))

	def test_ne(self):
		self.assertTrue(self.rectangle != Rectangle(1, 1, 1, 1))
		self.assertFalse(self.rectangle != Rectangle(0, 0, 4, 3))

	def test_center(self):
		self.assertEqual(self.rectangle.center(), Point(2, 1.5))

	def test_area(self):
		self.assertEqual(self.rectangle.area(), 25)

	def test_move(self):
		self.assertEqual(Rectangle.move(self.rectangle, 1, 1), Rectangle(1, 1, 5, 4))
		self.assertEqual(Rectangle.move(self.rectangle, -10, 2), Rectangle(-10, 2, -6, 5))

	def tearDown(self):
		del self.rectangle


if __name__ == '__main__':
	unittest.main()
