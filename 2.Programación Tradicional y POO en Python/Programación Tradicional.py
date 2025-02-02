# Programa para calcular el promedio semanal del clima y mostrar el resultado diario

def obtener_temperaturas():
    """
    Define las temperaturas diarias de la semana de forma predeterminada.
    Retorna una lista con las temperaturas y los días de la semana.
    """
    temperaturas = [20.5, 22.0, 19.8, 21.3, 23.1, 18.7, 20.0]  # Temperaturas predeterminadas
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return temperaturas, dias_semana

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de las temperaturas proporcionadas.
    Retorna el promedio semanal.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

def mostrar_resultados_diarios(temperaturas, dias_semana):
    """
    Muestra la temperatura ingresada para cada día de la semana.
    """
    print("\nTemperaturas ingresadas por día:")
    for dia, temp in zip(dias_semana, temperaturas):
        print(f"{dia}: {temp:.2f} grados")

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    print("\n--- Programa para calcular el promedio semanal del clima ---\n")

    # Obtener las temperaturas diarias
    temperaturas, dias_semana = obtener_temperaturas()

    # Mostrar resultados diarios
    mostrar_resultados_diarios(temperaturas, dias_semana)

    # Calcular el promedio semanal
    promedio = calcular_promedio(temperaturas)

    # Mostrar el resultado
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} grados.")

if __name__ == "__main__":
    main()
