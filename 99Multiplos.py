# Greet the User
print(f"---¡Bienvenido al programa, a continuación indica los números enteros a procesar!---\n")

nNumeros = 100

dato = [0 for rep in range(nNumeros)]

for rep in range(nNumeros):
    dato[rep] = int(input(f"Indica el número #{str(rep+1)}: \n"))
band = False

for rep in range(nNumeros - 1):
    if dato[rep] % dato[nNumeros - 1] == 0:
        band = True
if band:
    print(f"El número {dato[rep+1]} es múltiplo de alguno de los anteriores números")
else:
    print(f"El número {dato[rep+1]} *no* es múltiplo de alguno de los anteriores números")
