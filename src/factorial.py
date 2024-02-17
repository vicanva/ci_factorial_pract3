"""Mòdul per calcular el factorial d'un nombre."""

from math import factorial

class factorials:
    def factorial(self, n):
        """
        Calcula el factorial d'un nombre.

        Paràmetres:
            n (int): El nombre del qual es vol calcular el factorial.

        Retorna:
            int: El factorial de n.

        Excepcions:
            ValueError: Si n és negatiu.
            TypeError: Si n és decimal.
        """
        if n < 0:
            raise ValueError("No poden ser numeros negatius")

        if isinstance(n, float):
            raise TypeError("No val posar lletres")

        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
