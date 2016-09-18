import unittest
from primes import *


class PrimesTestCase(unittest.TestCase):
    """Tests for 'primes.py'."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_addition_integers(self):
        """Is integer addition 2 + 3 = 5?."""
        self.assertTrue(my_addition_function(2, 3))

    def test_addition_floats(self):
        """Is float addition 2.0 + 3.0 = 5?."""
        self.assertTrue(my_addition_function(2.0, 3.0))

    def test_addition_integer_string(self):
        """What happens when string is given as an input for addition?."""
        self.assertTrue(my_addition_function(2, 'refrigirator'))


if __name__ == '__main__':
    """Using Python's built-in unittest framework, any member function whose name begins with test
     in a class deriving from unittest.TestCase will be run, and its assertions checked,
     when unittest.main() is called"""
    unittest.main()
