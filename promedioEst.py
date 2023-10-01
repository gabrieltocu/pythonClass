
numeroEst = int(input("¿Cuántos son?: "))

aprueba = 0
noAprueba = 0
contador = 1
total = 0

while(contador <= numeroEst):
    notaEst = float(input("Indique la Nota del Estudiante: "))
    contador += 1
    total = total + notaEst
    if (notaEst >= 3):
        aprueba += 1
    else:
        noAprueba += 1
    media = total / numeroEst
print(aprueba, "estudiantes pasaron,", noAprueba, "no aprobaron.", "Y el promedio fue de", media)