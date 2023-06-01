# Importamos el modulo random
import random
print("Bienvenido al juego de piedra, papel o tijera!")
# variables de puntaje del usuario y de la computadora. Tambien creamos la de opciones
puntaje_usuario = 0
puntaje_computadora = 0

opciones = ["piedra", "papel", "tijera"]

# Bucle para que el usuario escriba su eleccion y le damos una tecla de salida
while True:
    usuario_input = input("Elija Piedra/Papel/Tijera o S para salir: ").lower()
    if usuario_input == "s":
        break

    # Creamos una lista para checkear si lo que selecciono el usuario esta o no en la lista
    if usuario_input not in opciones:
        continue

    # generamos el numero random(0:piedra, 1:papel y 2:tijera)
    numero_random = random.randint(0, 2)
    seleccion_computadora = opciones[numero_random]
    print("La computadora selecciono", seleccion_computadora + ".")

    # Comparamos lo que jugo el usuario vs la computadora para decidir quien gano
    if usuario_input == "piedra" and seleccion_computadora == "tijera":
        print("Tu ganas!")
        puntaje_usuario += 1

    elif usuario_input == "papel" and seleccion_computadora == "piedra":
        print("Tu ganas!")
        puntaje_usuario += 1

    elif usuario_input == "tijera" and seleccion_computadora == "papel":
        print("Tu ganas!")
        puntaje_usuario += 1
    else:
        print("Tu pierdes")
        puntaje_computadora += 1


# Mostramos la cantidad de veces que gano uno u el otro
print("Tu ganaste", puntaje_usuario, "veces.")
print("La computadora gano", puntaje_computadora, "veces.")
print("Hasta la próxima!")
