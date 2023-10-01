r = 3

nota = [0.0 for rep in range(r)]

nota = [0 for rep in range(r)]
for rep in range(r):
    nota[rep] = float(input('Indica la nota del estudiante: '))
    while nota[rep] < 0.0 or nota[rep] > 5.0:
        nota[rep] = float(input('Indica una nota entre 0 y 5: '))
est = int(input("Indica el estudiante que quieres bonificar: \n"))
while est < 1 or est > r:
    est = int(input("Indica el estudiante que quieres bonificar: "))
if nota[est-1] >= 5.0:
    nota[est-1] = 5.0
else:
    nota[est-1]+= 1
for rep in range(r):
    print(f'nota {rep+1} = {nota[rep]}')
