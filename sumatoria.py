# Greet the user
print("Bienvenido al usuario")

# Ask for a integer number
n = int(input("Dame el número para realizar la sumatoria: "))

sumatoria = 0

for rep in range(0, n+1, 1):
    sumatoria = sumatoria + (rep**2) + 8*rep
print("Sumatoria: ", sumatoria)