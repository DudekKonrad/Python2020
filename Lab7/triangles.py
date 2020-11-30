import unittest
from points import Point


class Triangle:

	def __init__(self, x1, y1, x2, y2, x3, y3):
		if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
			raise ValueError("Points are collinear")
		self.p1 = Point(x1, y1)
		self.p2 = Point(x2, y2)
		self.p3 = Point(x3, y3)

	def __str__(self):
		return "[({0}, {1}), ({2}, {3}), ({4}, {5})]".format(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)

	def __repr__(self):
		return "Triangle({0}, {1}, {2}, {3}, {4}, {5})".format(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)

	def __eq__(self, other):
		return self.p1 == other.p1 and self.p2 == other.p2 and self.p3 == other.p3

	def __ne__(self, other):
		return not self == other

	def center(self):
		return Point((self.p1.x + self.p2.x + self.p3.x) / 3, (self.p1.y + self.p2.y + self.p3.y) / 3)

	def area(self):
		return (1 / 2) * abs((self.p2.x - self.p1.x) * (self.p3.y - self.p1.y) - (self.p2.y - self.p1.y) * (self.p3.x - self.p1.x))

	def move(self, x, y):
		return Triangle(self.p1.x + x, self.p1.y + y, self.p2.x + x, self.p2.y + y, self.p3.x + x, self.p3.y + y)

	def make4(self):
		cp = self.center()
		triangles = [Triangle(cp.x, cp.y, self.p1.x, self.p1.y, self.p3.x, self.p3.y),
		             Triangle(self.p1.x, self.p1.y, self.p2.x, self.p2.y, cp.x, cp.y),
		             Triangle(self.p2.x, self.p2.y, cp.x, cp.y, self.p3.x, self.p3.y),
		             Triangle(self.p1.x, self.p1.y, cp.x, cp.y, (self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)]
		return triangles


class TestTriangle(unittest.TestCase):

	def setUp(self):
		self.triangle = Triangle(0, 0, 10, 5, 2, 10)

	def test_str(self):
		self.assertEqual(str(self.triangle), "[(0, 0), (10, 5), (2, 10)]")

	def test_repr(self):
		self.assertEqual(repr(self.triangle), "Triangle(0, 0, 10, 5, 2, 10)")

	def test_eq(self):
		self.assertTrue(self.triangle == Triangle(0, 0, 10, 5, 2, 10))
		self.assertTrue(self.triangle != Triangle(-3, 1, 7, 8, 5, 12))

	def test_center(self):
		self.assertEqual(Triangle.center(self.triangle), Point(4, 5))

	def test_area(self):
		self.assertEqual(Triangle.area(self.triangle), 45)

	def test_move(self):
		self.assertEqual(Triangle.move(self.triangle, 2, 4), Triangle(2, 4, 12, 9, 4, 14))
		self.assertEqual(Triangle.move(self.triangle, -2, 4), Triangle(-2, 4, 8, 9, 0, 14))
		self.assertEqual(Triangle.move(self.triangle, 2, -4), Triangle(2, -4, 12, 1, 4, 6))
		self.assertEqual(Triangle.move(self.triangle, -2, -4), Triangle(-2, -4, 8, 1, 0, 6))

	def test_make4(self):
		self.assertEqual(Triangle.make4(self.triangle),
		                 [Triangle(4, 5, 0, 0, 2, 10),
		                  Triangle(0, 0, 10, 5, 4, 5),
		                  Triangle(10, 5, 4, 5, 2, 10),
		                  Triangle(0, 0, 4, 5, 5, 2.5)])

	def tearDown(self):
		del self.triangle

if __name__ == '__main__':
	unittest.main()
