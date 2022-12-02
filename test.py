import unittest
from summa import sum_digits

class test(unittest.TestCase):
    def test_empty(self):
        n = sum_digits(9)
        self.assertEqual(sum_digits(n), 0)

if __name__ == '__main__':
    unittest.main()