
from math import factorial


class factorials:
    def factorial(self, n):
        if n < 0:
            raise ValueError("No poden ser numeros negatius")

        if  isinstance(n, float):
            raise TypeError("No val posar lletres")

        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

