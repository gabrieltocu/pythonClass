edad = int(input("Diga su edad: "))


while (0 > edad or edad > 120):
    edad = int(input("Diga una edad de 0 a 120: "))
if (edad < 18 and edad >= 0):
    print("Es menor de edad")
else:
    print("Es mayor de edad")

