import random

# Crear el Numero Secreto
numero_secreto = random.randint(1, 100)
# Inicializar Los Intentos
intentos = 0
jugar = 'si'

# Da la bienvenida
print("¡Bienvenido al juego de adivinar el número!")
# Indica el rango
print("Estoy pensando en un número entre 1 y 100.")


while jugar == 'si':
    suposicion = input("¿En qué número crees que estoy pensando? ")
    intentos += 1

    suposicion = int(suposicion)

    if suposicion < 1 or suposicion > 100:
        print("Por favor, ingresa un número entre 1 y 100.")
    elif suposicion < numero_secreto:
        print("El número secreto es mayor. Inténtalo de nuevo.")
    elif suposicion > numero_secreto:
        print("El número secreto es menor. Inténtalo de nuevo.")
    else:
        print(f"¡Felicitaciones! ¡Has adivinado el número secreto {numero_secreto} en {intentos} intentos!")
        jugar = input("¿Quieres jugar de nuevo? (si/no): ")
