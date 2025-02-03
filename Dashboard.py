import os


def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    opciones = {
        '1': '1.UNIDAD 1 POO 2425/Desarrollo de Ejemplos de Técnicas de Programación (POO).py',
        '2': '2.Programación Tradicional y POO en Python/Programación Orientada a Objetos (POO).py',
        '3': '2.Programación Tradicional y POO en Python/Programación Tradicional.py',
        '4': '3.Aplicación de Conceptos de POO en Python/vehiculos-poo.py',
        '5': '3.Tipos de datos, Identificadores/registro_estudiantes.py',
        '6': '4.EjemplosMundoReal_POO/Sistema de Alquiler de Vehículos.py',
        '7': '4.EjemplosMundoReal_POO/Sistema de Biblioteca.py',
        '8': '4.EjemplosMundoReal_POO/Sistema de Gestión de Pacientes en un Hospital.py',
        '9': '4.EjemplosMundoReal_POO/Sistema de Reservas de Hotel.py',
        '10': '4.EjemplosMundoReal_POO/Sistema de Tienda de Videojuegos.py',
        '11': '4.EjemplosMundoReal_POO/Tienda en Línea.py',
        '12': '5.Implementación de Constructores y Destructores en Python/Gestión de Objetos con Constructores y Destructores.py'
    }

    while True:
        print("\n******** Menu Principal - Dashboard *************")
        for key, value in opciones.items():
            print(f"{key} - {os.path.basename(value)}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            if os.path.exists(ruta_script):
                mostrar_codigo(ruta_script)
            else:
                print(f"El archivo {ruta_script} no existe o la ruta es incorrecta.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()
