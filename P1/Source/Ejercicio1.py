
import sys
import time


def calcular_promedio(numeros):
    """Calcula el promedio (mean) de una lista de números."""
    if len(numeros) == 0:
        return 0
    suma = 0
    for num in numeros:
        suma += num
    return suma / len(numeros)


def calcular_mediana(numeros):
    """Calcula la mediana (median) de una lista de números."""
    if len(numeros) == 0:
        return 0

    # Ordenar los números
    numeros_ordenados = sorted(numeros)
    cantidad = len(numeros_ordenados)

    # Si es par, promedio de los dos del centro
    if cantidad % 2 == 0:
        mediana = (numeros_ordenados[cantidad//2 - 1] +
                   numeros_ordenados[cantidad//2]) / 2
        return mediana

    return numeros_ordenados[cantidad//2]


def calcular_moda(numeros):
    """Calcula la moda (mode) - el número que más se repite."""
    if len(numeros) == 0:
        return None

    # Contar frecuencias manualmente
    frecuencias = {}
    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1

    # Encontrar el máximo
    max_frecuencia = 0
    moda = None
    for num, freq in frecuencias.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            moda = num

    return moda


def calcular_varianza(numeros, promedio):
    """Calcula la varianza de una lista de números."""
    if len(numeros) == 0:
        return 0

    suma_diferencias = 0
    for num in numeros:
        diferencia = num - promedio
        suma_diferencias += diferencia ** 2

    return suma_diferencias / len(numeros)


def calcular_desviacion_estandar(varianza):
    """Calcula la desviación estándar (raíz cuadrada de la varianza)."""
    return varianza ** 0.5


def main():
    """Función principal que procesa el archivo y calcula estadísticas."""
    # Verificar que se pasó un archivo como argumento
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar un archivo como argumento")
        print("Uso: python computeStatistics.py archivo.txt")
        return

    nombre_archivo = sys.argv[1]

    # Iniciar contador de tiempo
    tiempo_inicio = time.time()

    # Leer el archivo y procesar datos
    numeros = []
    errores = []

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea_num, linea in enumerate(archivo, 1):
                linea = linea.strip()
                if linea:  # Si la línea no está vacía
                    try:
                        numero = float(linea)
                        numeros.append(numero)
                    except ValueError:
                        error_msg = (f"Línea {linea_num}: '{linea}' "
                                     "no es un número válido")
                        errores.append(error_msg)
                        print(error_msg)

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return

    # Calcular estadísticas
    if len(numeros) == 0:
        print("No hay datos válidos para procesar")
        return

    promedio = calcular_promedio(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    varianza = calcular_varianza(numeros, promedio)
    desviacion = calcular_desviacion_estandar(varianza)

    # Calcular tiempo transcurrido
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio

    # Preparar resultados
    moda_str = str(moda) if moda is not None else 'N/A'
    resultados = f"""COUNT: {len(numeros)}
MEAN: {promedio}
MEDIAN: {mediana}
MODE: {moda_str}
SD: {desviacion}
VARIANCE: {varianza}

Tiempo de ejecución: {tiempo_total:.6f} segundos
"""

    # Mostrar en pantalla
    print("\n=== RESULTADOS ===")
    print(resultados)

    # Guardar en archivo
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(resultados)

    print("Resultados guardados en 'StatisticsResults.txt'")


if __name__ == "__main__":
    main()