contadorPos = 0
contadorNe = 0
numeros = 1

while (numeros <= 10):
    numero = int(input("Ingresa un número: "))
    numeros += 1
    if (numero >= 0):
        contadorPos += 1
    else:
        contadorNe += 1
print(contadorPos, "números positivos, y ", contadorNe, "números negativos")