# Saludar al Usuario
print("Bienvenido al programa!")

positivos = 0
negativos = 0
datos = 0

while (datos < 10):
    num = int(input("Ingresa un número: "))
    datos += 1
    if (num >= 0):
        positivos += 1
    else:
        negativos += 1
print(f"Tienes {negativos} números negativos, y {positivos} números positivos")