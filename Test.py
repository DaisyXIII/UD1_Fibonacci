#Programa principal donde definiremos una clase llamada Test donde probaremos nuestro software
import unittest
from fibo import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_secuencia_fibonacci(self):
        # Verificamos si el quinto número de la secuencia es igual a 3
        resultado = fibonacci(5)
        self.assertEqual(resultado[4],3)

if __name__ == '__main__':
    unittest.main()