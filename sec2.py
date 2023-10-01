
limInferior = 0
limSuperior = 0

while (limInferior >= limSuperior):
    limSuperior = int(input("Indica el límite superior (número entero): "))

    limInferior = int(input("Indica el límite inferior (número entero): "))

for rep in range(limInferior + 1, limSuperior, 1):
    print(rep, end=",")

