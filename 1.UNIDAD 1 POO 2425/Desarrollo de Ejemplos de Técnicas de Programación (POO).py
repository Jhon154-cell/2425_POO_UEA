from abc import ABC, abstractmethod

# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass  # Método abstracto que será implementado por las subclases

# Clase concreta: Rectángulo
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura  # Implementación específica

# Clase concreta: Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)  # Implementación específica

# Uso de las clases
rectangulo = Rectangulo(4, 5)
circulo = Circulo(3)

print("Área del rectángulo:", rectangulo.calcular_area())
print("Área del círculo:", circulo.calcular_area())

from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def realizar_pago(self, monto):
        pass

class TarjetaCredito(MetodoPago):
    def realizar_pago(self, monto):
        print(f"Pago de ${monto} realizado con tarjeta de crédito.")

class Paypal(MetodoPago):
    def realizar_pago(self, monto):
        print(f"Pago de ${monto} realizado con PayPal.")

# Uso
pago_tarjeta = TarjetaCredito()
pago_tarjeta.realizar_pago(100)

pago_paypal = Paypal()
pago_paypal.realizar_pago(200)

from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass

class Televisor(Dispositivo):
    def encender(self):
        print("El televisor se ha encendido.")

class Computadora(Dispositivo):
    def encender(self):
        print("La computadora se está iniciando.")

# Uso
tv = Televisor()
pc = Computadora()

tv.encender()
pc.encender()

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Se depositaron ${monto}. Saldo actual: ${self.__saldo}.")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se retiraron ${monto}. Saldo actual: ${self.__saldo}.")
        else:
            print("Fondos insuficientes.")

# Uso
cuenta = CuentaBancaria(500)
cuenta.depositar(200)
cuenta.retirar(100)

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Privado
        self.__edad = edad      # Privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

# Uso
persona = Persona("Carlos", 25)
print("Nombre actual:", persona.get_nombre())
persona.set_nombre("Juan")
print("Nuevo nombre:", persona.get_nombre())

class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a 0.")

# Uso
producto = Producto("Laptop", 1000)
print("Precio actual:", producto.get_precio())
producto.set_precio(1200)
print("Nuevo precio:", producto.get_precio())

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

# Uso
animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hablar())

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Auto(Vehiculo):
    def conducir(self):
        return f"Conduciendo un auto de marca {self.marca}."

# Uso
mi_auto = Auto("Toyota")
print(mi_auto.conducir())

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Gerente(Empleado):
    def supervisar(self):
        return f"El gerente {self.nombre} está supervisando."

# Uso
gerente = Gerente("María")
print(gerente.supervisar())

class Cuadrado:
    def area(self):
        return "Área = lado x lado"

class Triangulo:
    def area(self):
        return "Área = (base x altura) / 2"

# Uso
figuras = [Cuadrado(), Triangulo()]
for figura in figuras:
    print(figura.area())

class Guitarra:
    def tocar(self):
        return "Sonido de guitarra."

class Piano:
    def tocar(self):
        return "Sonido de piano."

# Uso
instrumentos = [Guitarra(), Piano()]
for instrumento in instrumentos:
    print(instrumento.tocar())

class Bicicleta:
    def mover(self):
        return "La bicicleta se mueve pedaleando."

class Avion:
    def mover(self):
        return "El avión se mueve volando."

# Uso
transportes = [Bicicleta(), Avion()]
for transporte in transportes:
    print(transporte.mover())
