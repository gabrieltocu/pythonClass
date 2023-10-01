# Número entero positivo

numero = int(input("Ingrese un número entero positivo: "))

factorial = 0

while (numero < 0):
    print("El número ingresado debe ser un entero positivo.")
    numero = int(input("Ingrese un número entero positivo: "))
if numero > 0:
    factorial = 1

    # Calcular el factorial utilizando
    for i in range(1, numero + 1):
        factorial *= i

    # Resultado
    print(f"El factorial de {numero} es {factorial}")
