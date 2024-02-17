import unittest

from src.factorial import factorials


class TestFactorial(unittest.TestCase):

    def test_factorial_1(self):
        """ probem que el factorial de 1 siga 1"""
        self.assertEqual(factorials.factorial(self,1), 1)

    def test_error_no_enter(self):
        """Probem que se pase un string"""
        with self.assertRaises(TypeError):
            factorials.factorial(self,"a")

    def test_error_num_negatiu(self):
        """Probem que se pase un numero negatiu"""
        with self.assertRaises(ValueError):
            factorials.factorial(self,-1)

    def test_factorial_5(self):
        """probem que el factorial de 5 es 120"""
        self.assertEqual(factorials.factorial(self,5), 120)


if __name__ == '__main__':
    unittest.main()
