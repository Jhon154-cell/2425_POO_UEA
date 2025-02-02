# 🏨 Sistema de Reservas de Hotel
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponible = True

    def ocupar(self):
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} ocupada.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        self.disponible = True
        print(f"Habitación {self.numero} liberada.")

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_reserva(self, habitacion):
        habitacion.ocupar()

    def cancelar_reserva(self, habitacion):
        habitacion.liberar()

# Ejecución del Sistema de Reservas de Hotel
habitacion1 = Habitacion(101, "Doble")
cliente1 = Cliente("Carlos")
cliente1.hacer_reserva(habitacion1)
cliente1.cancelar_reserva(habitacion1)
