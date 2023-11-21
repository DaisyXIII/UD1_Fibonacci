#Programa principal donde definiremos una clase llamada Test donde probaremos nuestro software
import unittest
from fibo import fibonacci

class Test(unittest.TestCase):

    def test_secuencia_fibonacci(self):
        # Pedimos por consola para poder hacer distintas pruebas sin modificar el código
        print("Qué posición desea comprobar?:")
        posicion = int(input())
        print("Dame el número que debería estar en esa posición:")
        numero = int(input())
        # Verificamos si el número de la posición indicada es igual al que hemos dado en la secuencia
        resultado = fibonacci(posicion)
        self.assertEqual(resultado[posicion-1],numero)

if __name__ == '__main__':
    unittest.main()