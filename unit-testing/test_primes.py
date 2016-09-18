import unittest
from primes import  is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for 'primes.py'."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))


if __name__ == '__main__':
    """Using Python's built-in unittest framework, any member function whose name begins with test
     in a class deriving from unittest.TestCase will be run, and its assertions checked,
     when unittest.main() is called"""
    unittest.main()
