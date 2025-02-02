'''
Programa: Registro Básico de Estudiantes
Función: Este programa permite gestionar un registro básico de estudiantes. Incluye opciones para
agregar, mostrar y buscar estudiantes en una lista. Utiliza diferentes tipos de datos como
integer, float, string y boolean.
'''

# Función para agregar un estudiante al registro
def agregar_estudiante(registro, nombre, edad, promedio, activo):
    """
    Agrega un estudiante al registro.
    :param registro: Lista que almacena los datos de los estudiantes.
    :param nombre: Nombre del estudiante (string).
    :param edad: Edad del estudiante (integer).
    :param promedio: Promedio del estudiante (float).
    :param activo: Estado del estudiante (boolean).
    """
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio,
        "activo": activo
    }
    registro.append(estudiante)
    print(f"Estudiante {nombre} agregado correctamente.")


# Función para mostrar todos los estudiantes del registro
def mostrar_estudiantes(registro):
    """
    Muestra todos los estudiantes almacenados en el registro.
    :param registro: Lista que almacena los datos de los estudiantes.
    """
    if registro:
        print("\nLista de estudiantes:")
        for i, estudiante in enumerate(registro, start=1):
            estado = "Activo" if estudiante["activo"] else "Inactivo"
            print(f"{i}. {estudiante['nombre']} - Edad: {estudiante['edad']}, "
                  f"Promedio: {estudiante['promedio']}, Estado: {estado}")
    else:
        print("\nNo hay estudiantes en el registro.")


# Función para buscar un estudiante por nombre
def buscar_estudiante(registro, nombre):
    """
    Busca un estudiante en el registro por su nombre.
    :param registro: Lista que almacena los datos de los estudiantes.
    :param nombre: Nombre del estudiante a buscar (string).
    """
    for estudiante in registro:
        if estudiante["nombre"].lower() == nombre.lower():
            estado = "Activo" if estudiante["activo"] else "Inactivo"
            print(f"\nEstudiante encontrado: {estudiante['nombre']} - Edad: {estudiante['edad']}, "
                  f"Promedio: {estudiante['promedio']}, Estado: {estado}")
            return
    print("\nEstudiante no encontrado.")


# Bloque principal del programa
if __name__ == "__main__":
    # Lista que almacenará el registro de estudiantes
    registro_estudiantes = []

    # Agregar algunos estudiantes al registro (datos iniciales)
    agregar_estudiante(registro_estudiantes, "Ana Pérez", 20, 8.7, True)
    agregar_estudiante(registro_estudiantes, "Luis Gómez", 22, 9.1, False)
    agregar_estudiante(registro_estudiantes, "María López", 19, 9.5, True)

    # Mostrar los estudiantes almacenados
    mostrar_estudiantes(registro_estudiantes)

    # Buscar un estudiante por nombre
    buscar_estudiante(registro_estudiantes, "Ana Pérez")
