import unittest
from sample import plus, multiply

def plus(a: int, b: int) -> int:
  """
  Возвращает результат сложения двух целых чисел.

  Args:
    a: Первое целое число.
    b: Второе целое число.

  Returns:
    Результат сложения a и b в виде целого числа.
  """
  return a + b

class TestPlus(unittest.TestCase):
    def test_plus_positive(self):
        self.assertEqual(plus(5, 3), 8)

    def test_plus_negative(self):
        self.assertEqual(plus(-5, 3), -2)

    def test_plus_zero(self):
        self.assertEqual(plus(5, 0), 5)

    def test_plus_large_numbers(self):
        self.assertEqual(plus(10000, 5000), 15000)

if __name__ == '__main__':
    unittest.main()

