import unittest
from carrito import Carrito

class TestCarrito(unittest.TestCase):
    def test_total(self):
        c = Carrito()
        c.agregar_producto("Clavos", 100, 2)
        self.assertEqual(c.calcular_total(), 200)

if __name__ == '__main__':
    unittest.main()
