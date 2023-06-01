# Bienvenido + nombre del usuario
nombre = input("Escribe tu nombre: ")
print("Bienvenido", nombre, "a tu aventura!")

# Primera eleccion
camino = input("Estas perdido en el medio del desierto y tienes que encontrar agua para sobrevivir, a lo lejos observas: 1) un lago. 2) un grupo de camellos. Hacia donde vas? 1/2? ")

camino = camino.lower()
# Condicional para eleccion 1 y sus caminos alternativos
if camino == "1":
    camino = input("Has llegado al supuesto lago, pero resulta que solo era un reflejo del sol, para tu suerte, te encuentras con un campamento con provisiones abandonadas, pero no hay agua. Que haces?: A) sigues por otro camino. B) Das la vuelta y vas donde los camellos.  Hacia donde vas? A/B? ")
    camino = camino.upper()

    if camino == "A":
        camino = input("Tomaste la decision de seguir por otro camino, en el transcurso encuentras a un hombre que tiene una cantimplora, le preguntas si te da pero este se niega. Tienes dos opciones: A) seguir de largo a la suerte. B) Sacarle la cantimplora a la fuerza.  Hacia donde vas? A/B? ")
        camino = camino.upper()

        if camino == "A":
            print("Has decidido seguir de largo a la suerte, pero para tu desgracia no encuentras agua y terminas muriendo deshidratado")
            quit()
        elif camino == "B":
            camino = input("Elegiste sacarle la cantimplora por la fuerza y terminas huyendo con ella pero resulta que esta esta vacia. a lo lejos, en direcciones opuestas miras que hay: A) un camello.  B) un campamento con una mochila.  Hacia donde vas? A/B? ")
            camino = camino.upper()
            if camino == "A":
                print("Has ido donde el camello, este estaba en un lago de agua que tu no podias ver, hidratate y escapa en camello del desierto!")
            elif camino == "B":
                print("Estas de suerte, la mochila contenia agua y un celular con red satelital por lo que puedes hacer una llamada para que te rescaten del desierto!")
            else:
                print("Mala decision, ese camino es invalido, has muerto!")
            quit()
        else:
            print("Mala decision, ese camino es invalido, has muerto!")

    elif camino == "B":
        print("Has decidido dar la vuelta e ir hacia donde los camellos, pero el camino es demasiado largo y mueres deshidratado en el camino")
# eleccion camino 2 con su final
elif camino == "2":
    print("Has decidido ir a por los camellos, para tu suerte estos estan en un lago que tu no podias ver, asi que te hidratas y usas los camellos para huir del desierto y asi sobrevives")
    print("Felicitaciones! Sobreviviste en el desierto!")
else:
    print("Mala decision, ese camino es invalido, has muerto!")
