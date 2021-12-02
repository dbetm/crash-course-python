import unittest
from unittest import TestCase
from testing_primes import is_prime


class TestingFunctions(TestCase):

    def test_is_prime(self):
        """ Testing is_prime method
        """

        self.assertEqual(is_prime(100), False)
        self.assertEqual(is_prime(42), False)
        self.assertEqual(is_prime(53), True)
        self.assertEqual(is_prime(3), True)


if __name__ == '__main__':
    unittest.main()
