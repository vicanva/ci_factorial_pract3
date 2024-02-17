import unittest
from pract3.src.factorial import factorials


class TestSuma(unittest.TestCase):

    def test_factorial_1(self):
        self.assertEqual(factorials.factorial(self,1), 1)

    def test_error_no_enter(self):
        with self.assertRaises(TypeError):
            factorials.factorial(self,"a")

    def test_error_num_negatiu(self):
        with self.assertRaises(ValueError):
            factorials.factorial(self,-1)

    def test_factorial_5(self):
        self.assertEqual(factorials.factorial(self,5), 120)

if __name__ == '__main__':
    unittest.main()
