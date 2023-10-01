suma = 0
r = 10

dato = [0 for rep in range(r)]
for rep in range(r):
    dato[rep] = int(input("Dime un número entero: "))
    suma = suma + dato[rep]
prom = suma / r
cont = 0
for rep in range(r):
    if dato[rep] > prom:
        cont += 1
print(f"Hay {cont} números mayores al promedio")


