# 🚗 Sistema de Alquiler de Vehículos
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} {self.modelo} ha sido alquilado.")
        else:
            print(f"El vehículo {self.marca} {self.modelo} no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El vehículo {self.marca} {self.modelo} ha sido devuelto.")

# Ejecución del Sistema de Alquiler de Vehículos
vehiculo1 = Vehiculo("Toyota", "Corolla")
vehiculo1.alquilar()
vehiculo1.devolver()
