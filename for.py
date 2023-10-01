# Ask the number to create the table
numero = int(input("¿Cuál es el número entero del cual quiere crear la tabla?: "))

for i in range(0, 10, 1):
    print(f"{numero} x {i} = {numero*i}")

