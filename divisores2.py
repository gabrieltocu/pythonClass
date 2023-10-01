contador = 0
n = int(input("¿Número?: "))


for rep in range(1, n+1):
    if (n % rep) == 0:
        contador += 1
        print(rep, "divisor")
print(f"El", n, "tiene",  contador,  "divisores")
