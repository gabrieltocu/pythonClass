import random

secreto = random.randint(1, 50)
intentos = 0

# Da la bienvenida
print("Bienvenido, Usuario")
# Indica el rango
print("Adivina el número entre 1 y 50")


while True:
    numero = input("Dime un número: ")
    intentos += 1

    numero = int(numero)

    if numero < 1 or numero > 100:
        print("Di un numero entre 1 y 50.")
    elif numero < secreto:
        print("El numero es mayor")
    elif numero > secreto:
        print("El numero es menor")
    else:
        print("El número secreto era ",numero, "y lo dijiste en ",intentos, "intentos")
        break
