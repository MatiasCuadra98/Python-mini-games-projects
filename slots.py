# importamos modulo
import random

# Creamos variables globales
LINEAS_MAXIMAS = 3
APUESTA_MAXIMA = 1000
APUESTA_MINIMA = 100
FILAS = 3
NUM_COLUMNAS = 3

# Creamos diccionarios
contador_simbolo = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

valor_simbolo = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# calculamos ganancias el jugador y las retornamos junto con lineas ganadoras


def confirmar_ganancias(columnas, lineas, apuesta, valores):
    ganadas = 0
    lineas_ganadoras = []

    for linea in range(lineas):
        simbolo = columnas[0][linea]
        for columna in columnas:
            confirmar_simbolo = columna[linea]
            if simbolo != confirmar_simbolo:
                break
        else:
            # Sumamos las ganancias de la línea a las ganancias totales
            ganadas += valores[simbolo] * apuesta
            lineas_ganadoras.append(linea + 1)

    return ganadas, lineas_ganadoras

# Creamos funcion para realizar una jugada


def generar_jugada(filas, columnas, simbolos):
    todos_los_simbolos = []

    # Creamos una lista con todos los símbolos basados en su cantidad
    for simbolo, contador_simbolo in simbolos.items():
        for _ in range(contador_simbolo):
            todos_los_simbolos.append(simbolo)

    columnas_generadas = []
    # Generamos las columnas seleccionando símbolos aleatorios
    for _ in range(columnas):
        columna = []
        simbolo_actual = todos_los_simbolos[:]
        for _ in range(filas):
            valor = random.choice(simbolo_actual)
            simbolo_actual.remove(valor)
            columna.append(valor)
        columnas_generadas.append(columna)

    return columnas_generadas


# Función para imprimir en pantalla las columnas

def mostrar_maquina_apuestas(columnas):
    for fila in range(len(columnas[0])):
        for i, columna in enumerate(columnas):
            if i != len(columnas) - 1:
                print(columna[fila], end=" | ")
            else:
                print(columna[fila], end="")

        print()


def cargar_dinero():
    respuesta = input(
        "No tienes balance suficiente. ¿Deseas cargar más dinero? (s/n): ")
    return respuesta.lower() == "s"


# Creamos una funcion para solicitarle al jugador el monto a depositar
def depositar():
    while True:
        cantidad = input("Cuanto quieres depositar? $")
        if cantidad.isdigit():  # para asegurar que el número que ingrese el usuario sea un dígito
            cantidad = int(cantidad)
            if cantidad > 0:
                break
            else:
                print("La cantidad debe ser mayor a 0.")
        else:
            print("Por favor ingrese un número.")
    return cantidad

# Funcion para solicitar al usuario las lineas en las que quiere apostar


def numero_de_lineas():
    while True:
        lineas = input(
            "Ingrese la cantidad de lineas en la que quiere apostar (1-" + str(LINEAS_MAXIMAS) + ")? ")
        if lineas.isdigit():
            lineas = int(lineas)
            if 1 <= lineas <= LINEAS_MAXIMAS:
                break
            else:
                print("Ingrese un numero valido de lineas.")
        else:
            print("Por favor ingrese un numero.")

    return lineas

# funcion para obtener la cantidad que quiere apostar en cada linea


def obtener_apuesta():
    while True:
        cantidad = input("Cuanto quieres apostar en cada linea? $")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if APUESTA_MINIMA <= cantidad <= APUESTA_MAXIMA:
                break
            else:
                print(
                    f"La cantidad a apostar debe ser entre ${APUESTA_MINIMA} - ${APUESTA_MAXIMA}.")
        else:
            print("Por favor ingrese un numero")
    return cantidad


# Funcion para realizar la jugada
def jugar(balance):
    lineas = numero_de_lineas()
    while True:
        apuesta = obtener_apuesta()
        apuesta_total = apuesta * lineas

        if apuesta_total > balance:
            print(
                f"Ustede no tiene suficiente balance para realizar esa apuesta, su balance actual es: ${balance}")
        else:
            break

    print(
        f"Ustede esta apostando ${apuesta} en {lineas} lineas. La apuesta total es: ${apuesta_total}"
    )

    # ponemos todas las funciones dentro de la main
    slots = generar_jugada(FILAS, NUM_COLUMNAS, contador_simbolo)
    mostrar_maquina_apuestas(slots)
    ganadas, lineas_ganadoras = confirmar_ganancias(
        slots, lineas, apuesta, valor_simbolo)
    print(f"Ganaste ${ganadas}.")
    print(f"Ganaste en las lineas:", *lineas_ganadoras)
    return ganadas - apuesta_total

# definimos la funcion principal del programa


def main():
    balance = depositar()
    while True:
        print(f"Tu balance actual es: ${balance}")
        pregunta = input("Presione enter para jugar o s para salir.")
        if pregunta == "s":
            break
        ganancias = jugar(balance)
        balance += ganancias

        if balance <= 0:
            print("No tienes balance suficiente para continuar jugando.")
            if cargar_dinero():
                balance = depositar()
            else:
                break

    print(f"Ustede termina con ${balance}")


main()
# iniciamos el programa llamando a la funcion principal
