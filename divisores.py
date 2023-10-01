cont = 0
numero = int(input("Dime el número a analizar: \n"))


for rep in range(1, numero+1):
    if (numero % rep) == 0:
        print(rep, "es divisor")
        cont += 1
print(f"El {numero} tiene  {cont}  divisores")
