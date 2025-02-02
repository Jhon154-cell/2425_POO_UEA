# 🏥 Sistema de Gestión de Pacientes en un Hospital
class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_medico = []

    def agregar_historial(self, nota):
        self.historial_medico.append(nota)
        print(f"Nota agregada al historial de {self.nombre}.")

class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def programar_cita(self, paciente, fecha):
        print(f"Cita programada para {paciente.nombre} con el Dr. {self.nombre} el {fecha}.")

# Ejecución del Sistema de Gestión de Pacientes
paciente1 = Paciente("Lucía", 30)
medico1 = Medico("Dr. Pérez", "Cardiología")
paciente1.agregar_historial("Consulta inicial: Sin complicaciones.")
medico1.programar_cita(paciente1, "12/01/2025")
