# Saludar al Usuario
print("Bienvenido al programa!")

pasan = 0
noPasan = 0
contador = 1
totalEstudiantes = 0

nEstudiantes = int(input("Indique el número de estudiantes en la clase: "))

while(contador <= nEstudiantes):
    notaEstudiante = float(input("Indique la Nota del Estudiante: "))
    contador += 1
    totalEstudiantes = totalEstudiantes + notaEstudiante
    if (notaEstudiante >= 3):
        pasan += 1
    else:
        noPasan += 1
    promedio = totalEstudiantes / nEstudiantes
print(f"{pasan} estudiantes aprobaron,y {noPasan} estudiantes reprobaron. La Clase tuvo un promedio acumulado de {promedio}")