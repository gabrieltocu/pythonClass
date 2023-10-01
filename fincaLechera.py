
prodM = 0
suma = 0

for rep in range(1, 51):
    prod = float(input(f'¿Cuántos litros produjo la vaca {rep}? '))

    suma += prod

    if prod > prodM:
        prodM = prod
        vaca = rep

media = suma / 50

print("La media es es: ", media, "litros por vaca", "la vaca más productiva dio: ", prodM, "litros")
