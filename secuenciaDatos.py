# Greet the User
print("Welcome")

ciclo = True


while (ciclo == True):
    # Ask for the first limit
    limSuperior = int(input("Indica el límite superior (número entero): "))

    # Ask for the second limit
    limInferior = int(input("Indica el límite inferior (número entero): "))

    if(limInferior >= limSuperior):
        print("Por favor indica los límites correctamente")
        ciclo = True
    else:
        ciclo = False

for rep in range(limInferior + 1, limSuperior, 1):
    print(rep, end=",")

