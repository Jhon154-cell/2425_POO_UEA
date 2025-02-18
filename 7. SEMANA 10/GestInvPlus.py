import os
import json


# Definición de la clase Producto, que representa un artículo en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Convierte el objeto Producto a un diccionario para facilitar la serialización en JSON
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    # Método estático para reconstruir un Producto a partir de un diccionario
    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

    # Representación en cadena del objeto Producto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario que maneja la lista de productos
class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()
        if not self.productos:
            self.precargar_productos()

    # Guarda los productos en un archivo JSON para persistencia
    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as f:
                json.dump([p.to_dict() for p in self.productos], f)
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")

    # Carga los productos desde un archivo JSON si existe
    def cargar_desde_archivo(self):
        if os.path.exists(self.ARCHIVO):
            try:
                with open(self.ARCHIVO, "r") as f:
                    data = json.load(f)
                    self.productos = [Producto.from_dict(p) for p in data]
            except (FileNotFoundError, json.JSONDecodeError):
                print("Error: Archivo de inventario corrupto o no encontrado.")

    # Agrega productos predeterminados al inventario si está vacío
    def precargar_productos(self):
        productos_precargados = [
            Producto(1, "Arroz", 50, 1.20),
            Producto(2, "Frijoles", 30, 2.50),
            Producto(3, "Leche", 20, 1.00),
            Producto(4, "Huevos", 60, 0.10),
            Producto(5, "Pan", 40, 0.50),
            Producto(6, "Azúcar", 25, 1.80),
            Producto(7, "Sal", 15, 0.90),
            Producto(8, "Café", 35, 3.50),
            Producto(9, "Aceite", 22, 4.00),
            Producto(10, "Harina", 28, 2.00)
        ]
        self.productos.extend(productos_precargados)
        self.guardar_en_archivo()

    # Agrega un nuevo producto si su ID no existe en el inventario
    def agregar_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    # Elimina un producto del inventario si el ID existe
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    # Actualiza la cantidad y/o precio de un producto si el ID existe
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    # Busca productos cuyo nombre contenga el texto ingresado
    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    # Muestra todos los productos almacenados en el inventario
    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


# Función principal que proporciona el menú interactivo

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Entrada inválida.")

        elif opcion == "2":
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: ID inválido.")

        elif opcion == "3":
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
                precio = input("Nuevo precio (deje vacío para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Entrada inválida.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
