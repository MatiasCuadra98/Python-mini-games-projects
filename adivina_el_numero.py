# Importamos modulo random para generar numeros random
import random
print("Bienvenido al juego de adivina el número!")
# creamos el input para que el usuario escriba el numero
rango_superior = input("Escribe un número: ")

# Creamos condicional para que el numero escrito por el jugador sea un numero y no otra cosa
if rango_superior.isdigit():
    rango_superior = int(rango_superior)
    if rango_superior <= 0:
        print("Por favor, ingrese un número mayor a 0.")
        quit()
else:
    print("Por favor, ingrese un número")
    quit()

# generamos el numero random con random.randint()
numero_random = random.randint(0, rango_superior)
# creamos al variable que cuenta las veces que el usuario adivino
adivinanzas = 0

# Creamos un bucle para decirle al usuario que haga su adivinanza y nos aseguramos que escriba un numero con isdigit()
while True:
    adivinanzas += 1
    adivinanzas_del_usuario = input("Adivina: ")
    if adivinanzas_del_usuario.isdigit():
        adivinanzas_del_usuario = int(adivinanzas_del_usuario)
    else:
        print("Por favor escriba un número.")
        continue
    # Le mostramos el mensaje de exito o fracaso al usuario
    if adivinanzas_del_usuario == numero_random:
        print("Lo clavaste!")
        break
    elif adivinanzas_del_usuario > numero_random:
        print("Estuviste mas arriba que el número, vuelve a intentarlo!")
    else:
        print("Estuviste por debajo del número, vuelve a intentarlo!")

# Mostramos al usuario las veces que adivino
print("Lo adivinaste en", adivinanzas, "intentos!")
