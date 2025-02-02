# Programa para calcular el promedio semanal del clima utilizando Programación Orientada a Objetos (POO)

class ClimaSemanal:
    """
    Clase que representa la información diaria del clima y calcula el promedio semanal.
    """

    def __init__(self):
        """
        Constructor que inicializa los datos del clima.
        """
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = [20.5, 22.0, 19.8, 21.3, 23.1, 18.7, 20.0]  # Temperaturas predeterminadas

    def mostrar_temperaturas(self):
        """
        Muestra las temperaturas de cada día de la semana.
        """
        print("\nTemperaturas diarias:")
        for dia, temp in zip(self.dias_semana, self.temperaturas):
            print(f"{dia}: {temp:.2f} grados")

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio semanal de las temperaturas.
        """
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    print("\n--- Programa para calcular el promedio semanal del clima utilizando POO ---\n")

    # Crear instancia de la clase ClimaSemanal
    clima_semanal = ClimaSemanal()

    # Mostrar temperaturas diarias
    clima_semanal.mostrar_temperaturas()

    # Calcular promedio semanal
    promedio = clima_semanal.calcular_promedio()

    # Mostrar resultado del promedio
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} grados.")

    # Comparación entre Programación Tradicional y POO
    print("\n--- Comparación de Programación Tradicional y POO ---")
    print("1. La Programación Tradicional organiza el código en funciones independientes, mientras que la POO utiliza clases para encapsular datos y comportamientos relacionados.")
    print("2. La POO permite reutilizar código y extender funcionalidades mediante herencia, algo que no es tan directo en la Programación Tradicional.")
    print("3. La POO facilita la organización de código en proyectos grandes, pero puede ser más compleja para problemas simples donde la Programación Tradicional es suficiente.")

if __name__ == "__main__":
    main()
