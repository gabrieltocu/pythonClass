# Iniciar suma en 0
suma = 0
# Obligar entrar al while
resp = "si"
# Instruccionaa repetitiva
while resp == "si":
    precio = int(input("Indique el precio: "))
    cant = int(input("Indique la cantidad del producto: "))

    suma = suma + cant*precio
    resp = input("¿Desea llevar otro producto? (si o no): ")
print(f"El total de la compra fue ${suma} pesos")
