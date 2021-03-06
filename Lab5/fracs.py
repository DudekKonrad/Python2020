import unittest


def NWD(a, b):
	a = a
	b = b
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a


def NWW(a, b):
	a = a
	b = b
	return a / NWD(a, b) * b


def add_frac(frac1, frac2):
	l1 = frac1[0]
	m1 = frac1[1]
	l2 = frac2[0]
	m2 = frac2[1]
	mianownik = NWW(m1, m2)
	pom = licznik = mianownik / m1 * l1 + mianownik / m2 * l2
	licznik /= NWD(pom, mianownik)
	mianownik /= NWD(pom, mianownik)
	result = [licznik, mianownik]
	return result


def sub_frac(frac1, frac2):
	l1 = frac1[0]
	m1 = frac1[1]
	l2 = frac2[0]
	m2 = frac2[1]
	mianownik = NWW(m1, m2)
	pom = licznik = mianownik / m1 * l1 - mianownik / m2 * l2
	licznik /= NWD(pom, mianownik)
	mianownik /= NWD(pom, mianownik)
	result = [licznik, mianownik]
	return result


def mul_frac(frac1, frac2):
	l1 = frac1[0]
	m1 = frac1[1]
	l2 = frac2[0]
	m2 = frac2[1]
	licznik = l1 * l2
	mianownik = m1 * m2
	n = NWD(licznik, mianownik)
	licznik /= n
	mianownik /= n
	result = [licznik, mianownik]
	return result


def div_frac(frac1, frac2):
	l1 = frac1[0]
	m1 = frac1[1]
	l2 = frac2[0]
	m2 = frac2[1]
	licznik = l1 * m2
	mianownik = m1 * l2
	n = NWD(licznik, mianownik)
	licznik /= n
	mianownik /= n
	result = [licznik, mianownik]
	return result


def is_positive(frac):
	negative = 0
	for item in frac:
		if item < 0:
			negative += 1
	if negative % 2 == 0:
		return True
	else:
		return False


def is_zero(frac):
	if frac[0] == 0 and frac[1] != 0:
		return True
	else:
		return False


def cmp_frac(frac1, frac2):
	l1 = frac1[0]
	m1 = frac1[1]
	l2 = frac2[0]
	m2 = frac2[1]
	mianownik = NWW(m1, m2)
	licznik1 = mianownik / m1 * l1
	licznik2 = mianownik / m2 * l2
	if licznik1 > licznik2:
		return 1
	elif licznik2 > licznik1:
		return -1
	elif licznik2 == licznik1:
		return 0


def frac2float(frac):
	result = frac[0] / frac[1]
	return result


class TestFractions(unittest.TestCase):

	def setUp(self):
		self.zero = [0, 1]

	def test_add_frac(self):
		self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
		self.assertEqual(add_frac([1, -2], [1, 3]), [-1, 6])
		self.assertEqual(add_frac([-1, -2], [1, 3]), [5, 6])
		self.assertEqual(add_frac([2, 4], [-1, 2]), [0, 1])
		self.assertEqual(add_frac([2, 4], [1, -2]), [0, 1])

	def test_sub_frac(self):
		self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
		self.assertEqual(sub_frac([1, -2], [1, 3]), [-5, 6])
		self.assertEqual(sub_frac([-1, -2], [1, 3]), [1, 6])
		self.assertEqual(sub_frac([2, 4], [-1, 2]), [1, 1])
		self.assertEqual(sub_frac([2, 4], [1, -2]), [1, 1])

	def test_mul_frac(self):
		self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
		self.assertEqual(mul_frac([-1, 3], [1, 6]), [-1, 18])

	def test_div_frac(self):
		self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
		self.assertEqual(div_frac([-1, 3], [1, 6]), [-2, 1])

	def test_is_positive(self):
		self.assertFalse(is_positive([1, -7]))
		self.assertFalse(is_positive([-1, 7]))
		self.assertTrue(is_positive([1, 7]))
		self.assertTrue(is_positive([-1, -7]))

	def test_is_zero(self):
		self.assertFalse(is_zero([1, 2]))
		self.assertFalse(is_zero([1, 3]))
		self.assertTrue(is_zero([0, 3]))
		self.assertTrue(is_zero([0, -2]))

	def test_cmp_frac(self):
		self.assertEqual(cmp_frac([1, 9], [2, 27]), 1)
		self.assertEqual(cmp_frac([2, 27], [1, 9]), -1)
		self.assertEqual(cmp_frac([1, 6], [1, 6]), 0)
		self.assertEqual(cmp_frac([-1, 6], [1, 6]), -1)
		self.assertEqual(cmp_frac([1, 6], [-1, 6]), 1)
		self.assertEqual(cmp_frac([1, 6], [1, -6]), 1)

	def test_frac2float(self):
		self.assertEqual(frac2float([1, 2]), 0.5)

	def tearDown(self):
		self.zero = None


if __name__ == '__main__':
	unittest.main()
