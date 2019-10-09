from unittest import TestCase

from primeproduct_03 import prime_product


class TestPrimeProduct(TestCase):
    def test_prime_product_01(self):
        self.assertEqual(prime_product(1), 0)

    def test_prime_product_02(self):
        self.assertEqual(prime_product(3), 0)

    def test_prime_product_03(self):
        self.assertEqual(prime_product(4), 4)

    def test_prime_product_04(self):
        self.assertEqual(prime_product(5), 6)

    def test_prime_product_05(self):
        self.assertEqual(prime_product(6), 9)

    def test_prime_product_06(self):
        self.assertEqual(prime_product(7), 10)

    def test_prime_product_07(self):
        self.assertEqual(prime_product(8), 15)

    def test_prime_product_08(self):
        self.assertEqual(prime_product(9), 14)

    def test_prime_product_09(self):
        self.assertEqual(prime_product(10), 25)

    def test_prime_product_10(self):
        self.assertEqual(prime_product(11), 0)

    def test_prime_product_11(self):
        self.assertEqual(prime_product(12), 35)

    def test_prime_product_12(self):
        self.assertEqual(prime_product(20), 91)

    def test_prime_product_13(self):
        self.assertEqual(prime_product(100), 2491)
