import random
def cachipun():
    usuario = input("Elige piedra, papel o tijera: ")
    computador = ["piedra","papel","tijera"]
    elec = random.choice(computador)
    if usuario == elec:
        print("Lo siento, fue empate")
    else:
        if usuario == "piedra" and elec == "tijera":
            print("Ganaste!!")
        elif usuario == "tijera" and elec == "papel":
            print("Ganaste!!")
        elif usuario == "papel" and elec == "piedra":
            print("Ganaste!!")
        elif usuario == "tijera" and elec == "piedra":
            print("Gane")
        elif usuario == "piedra" and elec == "papel":
            print("Gane")
        elif usuario == "papel" and elec == "tijera":
            print ("Gane")
        else:
            print("Nadie gana")

    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    pass