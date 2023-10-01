# Saludar al usuario
print("Bienvenido al programa!")

# Iniciar los datos
datos = 0
suma = 0

while (datos < 100):
    # Pedir un número entero
    num = int(input("Ingrese un número entero: "))
    suma = suma + num
    datos += 1
print(f"La suma total de los números es {suma}")
