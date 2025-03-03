import json  # Importamos la librería para manejar archivos JSON


class Producto:
    # Clase que representa un producto en el inventario
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario
        self.precio = precio  # Precio del producto

    def actualizar_cantidad(self, nueva_cantidad):
        # Método para actualizar la cantidad del producto
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        # Método para actualizar el precio del producto
        self.precio = nuevo_precio

    def obtener_info(self):
        # Método para obtener la información del producto en formato de cadena
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    # Clase que gestiona los productos en el inventario
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos usando el ID como clave

    def agregar_producto(self, producto):
        # Método para añadir un producto al inventario
        self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        # Método para eliminar un producto del inventario por su ID
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Método para actualizar la cantidad o el precio de un producto
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Método para buscar productos por nombre (insensible a mayúsculas/minúsculas)
        return [p.obtener_info() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_productos(self):
        # Método para mostrar todos los productos en el inventario
        return [p.obtener_info() for p in self.productos.values()]

    def guardar_en_archivo(self, archivo="inventario.json"):
        # Método para guardar el inventario en un archivo JSON (serialización)
        with open(archivo, "w") as f:
            json.dump({id_prod: vars(prod) for id_prod, prod in self.productos.items()}, f)

    def cargar_desde_archivo(self, archivo="inventario.json"):
        # Método para cargar el inventario desde un archivo JSON (deserialización)
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.productos = {id_prod: Producto(**prod) for id_prod, prod in datos.items()}
        except FileNotFoundError:
            print("Archivo de inventario no encontrado.")


def menu():
    # Función que muestra el menú interactivo en la consola
    inventario = Inventario()
    inventario.cargar_desde_archivo()  # Cargamos los datos del inventario si existen

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")  # Solicitamos al usuario que seleccione una opción

        if opcion == "1":
            # Agregar un nuevo producto al inventario
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            # Eliminar un producto del inventario
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            # Actualizar un producto existente en el inventario
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se actualiza): ")
            precio = input("Nuevo precio (dejar en blanco si no se actualiza): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            # Buscar productos por nombre
            nombre = input("Nombre del producto: ")
            print("\n".join(inventario.buscar_producto(nombre)))
        elif opcion == "5":
            # Mostrar todos los productos en el inventario
            print("\n".join(inventario.mostrar_productos()))
        elif opcion == "6":
            # Guardar el inventario en un archivo y salir del programa
            inventario.guardar_en_archivo()
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()  # Ejecutamos el menú principal
