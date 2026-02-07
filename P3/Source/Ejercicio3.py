
import sys
import time


def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto.
    Retorna un diccionario con palabra:frecuencia.
    """
    palabras = texto.lower().split()

    frecuencias = {}

    for palabra in palabras:
        palabra_limpia = ""
        for caracter in palabra:
            if caracter.isalnum():
                palabra_limpia += caracter

        if palabra_limpia:
            if palabra_limpia in frecuencias:
                frecuencias[palabra_limpia] += 1
            else:
                frecuencias[palabra_limpia] = 1

    return frecuencias


def main():
    """Función principal que procesa el archivo y cuenta palabras."""
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar un archivo como argumento")
        print("Uso: python wordCount.py archivo.txt")
        return

    nombre_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return
    except UnicodeDecodeError:
        print(f"Error: No se pudo leer el archivo '{nombre_archivo}'")
        return

    if not contenido.strip():
        print("El archivo está vacío")
        return

    frecuencias = contar_palabras(contenido)

    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio

    palabras_ordenadas = sorted(frecuencias.items())

    resultados = "=== FRECUENCIA DE PALABRAS ===\n\n"

    for palabra, frecuencia in palabras_ordenadas:
        resultados += f"{palabra}: {frecuencia}\n"

    resultados += f"\n\nTotal de palabras distintas: {len(frecuencias)}\n"
    total_palabras = sum(frecuencias.values())
    resultados += f"Total de palabras en el archivo: {total_palabras}\n"
    resultados += f"Tiempo de ejecución: {tiempo_total:.6f} segundos\n"

    print(resultados)

    with open('WordCountResults.txt', 'w', encoding='utf-8') as salida:
        salida.write(resultados)

    print("Resultados guardados en 'WordCountResults.txt'")


if __name__ == "__main__":
    main()