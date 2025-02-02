# Clase base que representa un Vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.modelo = modelo  # Atributo público
        self.__encendido = False  # Atributo privado para demostrar encapsulación

    # Método público para encender el vehículo
    def encender(self):
        self.__encendido = True
        print(f"El vehículo {self.marca} {self.modelo} está encendido.")

    # Método público para apagar el vehículo
    def apagar(self):
        self.__encendido = False
        print(f"El vehículo {self.marca} {self.modelo} está apagado.")

    # Método protegido para verificar si el vehículo está encendido
    def _estado_encendido(self):
        return self.__encendido


# Clase derivada que representa un Automóvil, hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, tipo_combustible):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.tipo_combustible = tipo_combustible  # Atributo adicional de la clase hija

    # Método sobrescrito (polimorfismo mediante sobreescritura)
    def encender(self):
        if not self._estado_encendido():
            super().encender()  # Llamada al método de la clase base
            print(f"El automóvil funciona con {self.tipo_combustible}.")
        else:
            print(f"El automóvil {self.marca} {self.modelo} ya está encendido.")


# Clase derivada que representa una Moto, hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_casco):
        super().__init__(marca, modelo)
        self.tipo_casco = tipo_casco

    # Método sobrescrito para demostrar polimorfismo
    def encender(self):
        if not self._estado_encendido():
            super().encender()
            print(f"Recuerda usar un casco {self.tipo_casco} al conducir.")
        else:
            print(f"La moto {self.marca} {self.modelo} ya está encendida.")


# Instanciamos objetos y demostramos las funcionalidades
if __name__ == "__main__":
    # Creación de un automóvil
    auto = Automovil("Toyota", "Corolla", "Gasolina")
    auto.encender()  # Llamada al método sobrescrito
    auto.apagar()

    # Creación de una moto
    moto = Moto("Yamaha", "R15", "integral")
    moto.encender()  # Llamada al método sobrescrito
    moto.apagar()
