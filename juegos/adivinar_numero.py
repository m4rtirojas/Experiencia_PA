import random
def adivinar_numero():
    pc = random.randint(1,10)
    user = int(input("Elige un numero del 1 al 10: "))
    if pc == user:
        print("Has adivinado! Felicitaciones!!")
    else:
        print("No has adivinado, suerte para la proxima")
    
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    pass