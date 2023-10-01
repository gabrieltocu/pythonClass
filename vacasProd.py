total = 0
p_max = 0

for rep in range(1, 51):
    produccion = float(input(f'¿Cuántos litros produjo la vaca {rep}? '))

    total += produccion

    if produccion > p_max:
        p_max = produccion
        vaca_max = rep

promedio = total / 50

print(f'El promedio de producción de la finca es: {promedio} litros por vaca.')
print(f'La vaca más productiva fue la número {vaca_max} con {p_max} litros.')
