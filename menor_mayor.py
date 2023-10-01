# Greet the User
print("Bienvenido al programa")

ageU = int(input("Indica la edad: "))


while (ageU < 0 or ageU > 120):
    ageU = int(input("Indica una edad entre 0 y 120 años: "))
if (ageU >= 18 and ageU <= 120):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")



