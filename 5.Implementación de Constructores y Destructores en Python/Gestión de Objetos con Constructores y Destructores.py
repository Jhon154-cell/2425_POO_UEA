# Clase 1: Usuario
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        print(f"Usuario {self.nombre} creado con email {self.email}.")

    def __del__(self):
        print(f"Usuario {self.nombre} eliminado.")

# Clase 2: Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        print(f"Producto {self.nombre} creado con precio ${self.precio}.")

    def __del__(self):
        print(f"Producto {self.nombre} eliminado.")

# Clase 3: Orden
class Orden:
    def __init__(self, id_orden, productos):
        self.id_orden = id_orden
        self.productos = productos
        print(f"Orden {self.id_orden} creada con {len(productos)} productos.")

    def __del__(self):
        print(f"Orden {self.id_orden} eliminada.")

# Clase 4: CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        print(f"Cuenta bancaria de {self.titular} creada con saldo ${self.saldo}.")

    def __del__(self):
        print(f"Cuenta bancaria de {self.titular} cerrada.")

# Clase 5: Biblioteca
class Biblioteca:
    def __init__(self, nombre, libros):
        self.nombre = nombre
        self.libros = libros
        print(f"Biblioteca {self.nombre} creada con {len(libros)} libros.")

    def __del__(self):
        print(f"Biblioteca {self.nombre} eliminada.")

# Clase 6: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"Vehículo {self.marca} {self.modelo} creado.")

    def __del__(self):
        print(f"Vehículo {self.marca} {self.modelo} eliminado.")

# Clase 7: Sensor
class Sensor:
    def __init__(self, tipo, unidad):
        self.tipo = tipo
        self.unidad = unidad
        print(f"Sensor de tipo {self.tipo} creado, mide en {self.unidad}.")

    def __del__(self):
        print(f"Sensor de tipo {self.tipo} eliminado.")

# Clase 8: Computadora
class Computadora:
    def __init__(self, procesador, ram):
        self.procesador = procesador
        self.ram = ram
        print(f"Computadora con procesador {self.procesador} y RAM {self.ram} creada.")

    def __del__(self):
        print(f"Computadora con procesador {self.procesador} eliminada.")

# Clase 9: Curso
class Curso:
    def __init__(self, nombre, estudiantes):
        self.nombre = nombre
        self.estudiantes = estudiantes
        print(f"Curso {self.nombre} creado con {len(estudiantes)} estudiantes.")

    def __del__(self):
        print(f"Curso {self.nombre} eliminado.")

# Clase 10: Animal
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
        print(f"Animal de especie {self.especie} creado, tiene {self.edad} años.")

    def __del__(self):
        print(f"Animal de especie {self.especie} eliminado.")

# Ejemplo de creación y eliminación
usuario = Usuario("Juan", "juan@example.com")
producto = Producto("Laptop", 1500.0)
orden = Orden(1234, [producto])
cuenta = CuentaBancaria("María", 5000.0)
biblioteca = Biblioteca("Central", ["Libro1", "Libro2"])
vehiculo = Vehiculo("Toyota", "Corolla")
sensor = Sensor("Temperatura", "Celsius")
computadora = Computadora("Intel i7", "16GB")
curso = Curso("Matemáticas", ["Estudiante1", "Estudiante2"])
animal = Animal("Gato", 3)

# Nota: Los destructores se activan cuando el objeto es eliminado o al finalizar el programa.
