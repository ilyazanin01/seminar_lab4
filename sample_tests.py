import unittest
from sample import plus

class TestPlus(unittest.TestCase):
    def test_plus_positive(self):
        self.assertEqual(plus(5, 3), 8)

    def test_plus_negative(self):
        self.assertEqual(plus(-5, 3), -2)

    def test_plus_zero(self):
        self.assertEqual(plus(5, 0), 5)

    def test_plus_large_numbers(self):
        self.assertEqual(plus(10000, 5000), 15000)
