
numero = int(input("Ingrese un número entero positivo: "))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print("El factorial es", factorial )
