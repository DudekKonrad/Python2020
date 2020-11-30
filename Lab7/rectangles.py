from points import Point
import unittest
import math


class Rectangle:

	def __init__(self, x1, y1, x2, y2):
		if y2 <= y1 or x2 <= x1:
			raise ValueError("Position of points must be x1 < x2 and y1 < y2")
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
		return math.fabs(self.pt1.x - self.pt2.x) * math.fabs(self.pt1.y - self.pt2.y)

	def move(self, x, y):  # przesunięcie o (x, y)
		return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

	def intersection(self, other):
		point1 = Point(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y))
		point2 = Point(min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
		if point2.x <= point1.x or point2.y <= point1.y:
			raise ValueError(
				"Points should be x1 < x2 and y1 < y2")
		return Rectangle(point1.x, point1.y, point2.x, point2.y)

	def cover(self, other):
		point1 = Point(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y))
		point2 = Point(max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
		if point2.x <= point1.x or point2.y <= point1.y:
			raise ValueError(
				"not valid value in rectangle due to the fact that it should contain points where: x1 < x2 and y1 < y2")
		return Rectangle(point1.x, point1.y, point2.x, point2.y)

	def make4(self):
		center_point = self.center()
		rectangles = [Rectangle(center_point.x, center_point.y, self.pt2.x, self.pt2.y),
		              Rectangle(center_point.x, self.pt1.y, self.pt2.x, center_point.y),
		              Rectangle(self.pt1.x, center_point.y, center_point.x, self.pt2.y),
		              Rectangle(self.pt1.x, self.pt1.y, center_point.x, center_point.y)]
		return rectangles


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
		self.assertTrue(self.rectangle != Rectangle(1, 1, 2, 2))
		self.assertFalse(self.rectangle != Rectangle(0, 0, 4, 3))

	def test_center(self):
		self.assertEqual(self.rectangle.center(), Point(2, 1.5))

	def test_area(self):
		self.assertEqual(self.rectangle.area(), 12)

	def test_move(self):
		self.assertEqual(Rectangle.move(self.rectangle, 2, 4), Rectangle(2, 4, 6, 7))
		self.assertEqual(Rectangle.move(self.rectangle, -2, 4), Rectangle(-2, 4, 2, 7))
		self.assertEqual(Rectangle.move(self.rectangle, 2, -4), Rectangle(2, -4, 6, -1))
		self.assertEqual(Rectangle.move(self.rectangle, -2, -4), Rectangle(-2, -4, 2, -1))

	def test_intersection(self):
		self.assertEqual(Rectangle.intersection(self.rectangle, Rectangle(-3, -2, 5, 1)), Rectangle(0, 0, 4, 1))
		with self.assertRaises(ValueError):
			Rectangle.intersection(self.rectangle, Rectangle(5, 8, 4, 1))

	def test_cover(self):
		self.assertEqual(Rectangle.cover(self.rectangle, Rectangle(2, 3, 8, 14)), Rectangle(0, 0, 8, 14))
		with self.assertRaises(ValueError):
			Rectangle.intersection(self.rectangle, Rectangle(1, -5, 5, -1))

	def test_make4(self):
		self.assertEqual(Rectangle.make4(self.rectangle),
		                 [Rectangle(2, 1.5, 4, 3),
		                  Rectangle(2, 0, 4, 1.5),
		                  Rectangle(0, 1.5, 2, 3),
		                  Rectangle(0, 0, 2, 1.5)])

	def tearDown(self):
		del self.rectangle


if __name__ == '__main__':
	unittest.main()
