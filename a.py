# Suma
suma = 0
# El while
resp = "si"
# Instrucción
while resp == "si":
    precio = int(input("Indique el precio: "))
    cant = int(input("Indique la cantidad del producto: "))

    suma = suma + cant*precio
    resp = input("¿Desea llevar otro producto? (si o no): ")
print("El total de la compra fue", suma, "pesos")