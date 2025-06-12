class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        self.productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})

    def calcular_total(self):
        return sum(p['precio'] * p['cantidad'] for p in self.productos)
