# Bienvenida!
print("Bienvenido a mi juego de preguntas sobre cultura general!")
# Comienzo del juego
jugar = input("Quieres comenzar a jugar? ")

if jugar.lower() != "si":
    quit()
print("Okay! Comencemos a jugar!")
# variable para asignar le puntaje del jugador
puntaje = 0

# Preguntas al jugador

pregunta = input("Cuál es la capital de Argentina? ")
if pregunta.lower() == "Buenos Aires":
    print("Correcto!")
    puntaje += 1
else:
    print("Incorrecto!")

pregunta = input("Cuál es el lugar mas frío de la tierra? ")
if pregunta.lower() == "La Antártida":
    print("Correcto!")
    puntaje += 1

else:
    print("Incorrecto!")

pregunta = input("Cuál es el río mas largo del mundo? ")
if pregunta.lower() == "El Amazonas":
    print("Correcto")
    puntaje += 1

else:
    print("Incorrecto!")

pregunta = input("En que año el hombre llegó a la Luna? ")
if pregunta.lower() == "1969":
    print("Correcto")
    puntaje += 1

else:
    print("Incorrecto!")

pregunta = input("Cuantos países hay en el mundo? ")
if pregunta.lower() == "195":
    print("Correcto")
    puntaje += 1

else:
    print("Incorrecto!")


# calculamos el puntaje total y tambien se lo mostramos en porcentaje
print("Tienes " + str(puntaje) + " respuestas correctas!")
print("Conseguiste un " + str((puntaje/5) * 100) + "%. ")
