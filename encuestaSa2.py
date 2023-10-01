respuestas = 'si'
conteoS = 0
conteoN = 0

while respuestas == 'si':
    respuesta = input("Estuvo buena la conferencia? si/no: ").lower()
    if respuesta == 'si':
        conteoS += 1
    elif respuesta == 'no':
        conteoN += 1
    else:
        print("Di: 'si' o 'no'")

    respuestas = input("Hay alguien sin responder? si/no: ").lower()

suma = conteoS + conteoN

# Calcular porcentajes
porcentajeS = (conteoS / suma) * 100
porcentajeN = (conteoN / suma) * 100

print("Al", porcentajeS, "le gustó, y al", porcentajeN, "no le gustó la conferencia")
