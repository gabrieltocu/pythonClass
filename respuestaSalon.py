estudiantes = int(input("¿Cuántos estudiantes hay en la clase?: "))
n = True

while estudiantes <= 0:
    estudiantes = int(input("Indica de nuevo la cantidad de estudiantes: "))

estArr = [0 for rep in range(estudiantes)]

for rep in range(estudiantes):
    estArr[rep] = float(input(f"Estudiante #{str(rep+1)}, ¿Cuál crees que es la resputasta?: "))
prof = float(input("Profesor, ¿Cuál es la respuseta correcta?\n"))
for rep in range(estudiantes):
    if estArr[rep] == prof:
        print(f"El estudiante #{rep+1} contestó correctamente!!")
        n = False
if n:
    print("Ningún contestó correctamente")
