class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Constructor para inicializar un producto con ID único, nombre, cantidad y precio
        # Se usa la técnica de encapsulamiento al definir atributos privados con métodos de acceso
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters (acceso controlado a los atributos)
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters (modificación controlada de los atributos)
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        # Representación en cadena del producto para facilitar su visualización
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        # Inicializa una lista vacía de productos
        # Se usa una estructura de datos tipo lista para almacenar múltiples productos
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un producto si el ID es único
        # Se utiliza comprensión de listas para verificar unicidad del ID
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id):
        # Elimina un producto por su ID utilizando una estructura de control iterativa
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Actualiza la cantidad y/o el precio de un producto mediante parámetros opcionales
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # Busca productos por nombre (puede haber nombres similares)
        # Se utiliza comprensión de listas para filtrar los productos
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Muestra todos los productos en el inventario usando un bucle for
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    # Interfaz de usuario en consola utilizando un menú interactivo
    inventario = Inventario()

    # Agregamos algunos productos iniciales para pruebas
    inventario.agregar_producto(Producto(1, "Manzana", 50, 0.5))
    inventario.agregar_producto(Producto(2, "Banana", 100, 0.3))
    inventario.agregar_producto(Producto(3, "Naranja", 75, 0.6))

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
                # Solicitud de datos utilizando entradas del usuario
                id = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Entrada inválida. Asegúrese de ingresar números en ID, cantidad y precio.")

        elif opcion == "2":
            try:
                # Eliminación de producto usando control de excepciones
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        elif opcion == "3":
            try:
                # Actualización de atributos con entradas opcionales
                id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Entrada inválida. Asegúrese de ingresar números en ID, cantidad y precio.")

        elif opcion == "4":
            # Búsqueda de productos usando coincidencias parciales de nombre
            nombre = input("Ingrese el nombre o parte del nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            # Mostrar el listado completo de productos
            inventario.mostrar_todos()

        elif opcion == "6":
            # Salida controlada del sistema
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    # Punto de entrada principal del programa
    menu()
