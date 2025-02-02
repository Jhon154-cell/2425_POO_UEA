# 🛒 Tienda en Línea
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0

    def agregar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Se agregaron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

    def vender(self):
        if self.stock > 0:
            self.stock -= 1
            print(f"Se vendió una unidad de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay stock de {self.nombre} disponible.")

# Ejecución de la Tienda en Línea
producto1 = Producto("Laptop", 800)
producto1.agregar_stock(10)
producto1.vender()
producto1.vender()
