
import sys
import time


def decimal_a_binario(numero):
    """Convierte un número decimal a binario usando algoritmo manual."""
    if numero == 0:
        return "0"

    binario = ""
    num_abs = abs(int(numero))

    while num_abs > 0:
        residuo = num_abs % 2
        binario = str(residuo) + binario
        num_abs = num_abs // 2

    if numero < 0:
        binario = "-" + binario

    return binario


def decimal_a_hexadecimal(numero):
    """Convierte un número decimal a hexadecimal usando algoritmo manual."""
    if numero == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num_abs = abs(int(numero))

    while num_abs > 0:
        residuo = num_abs % 16
        hexadecimal = hex_chars[residuo] + hexadecimal
        num_abs = num_abs // 16

    if numero < 0:
        hexadecimal = "-" + hexadecimal

    return hexadecimal


def main():
    """Función principal que procesa el archivo y convierte números."""
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar un archivo como argumento")
        print("Uso: python convertNumbers.py archivo.txt")
        return

    nombre_archivo = sys.argv[1]
    tiempo_inicio = time.time()
    conversiones = []

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea_num, linea in enumerate(archivo, 1):
                linea = linea.strip()
                if linea:
                    try:
                        numero = float(linea)
                        binario = decimal_a_binario(numero)
                        hexadecimal = decimal_a_hexadecimal(numero)
                        conversiones.append(
                            f"Decimal: {int(numero)} | "
                            f"Binario: {binario} | "
                            f"Hexadecimal: {hexadecimal}"
                        )
                    except ValueError:
                        error_msg = (f"Línea {linea_num}: '{linea}' "
                                     "no es un número válido")
                        print(error_msg)

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return

    if len(conversiones) == 0:
        print("No hay datos válidos para procesar")
        return

    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio

    resultados = "\n".join(conversiones)
    resultados += f"\n\nTiempo de ejecución: {tiempo_total:.6f} segundos\n"
    resultados += f"Total de números convertidos: {len(conversiones)}\n"

    print("\n=== RESULTADOS DE CONVERSIÓN ===")
    print(resultados)

    with open('ConvertionResults.txt', 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(resultados)

    print("Resultados guardados en 'ConvertionResults.txt'")


if __name__ == "__main__":
    main()