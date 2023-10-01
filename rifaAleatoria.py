import random

# Greet the User
print(f"Welcome to the random raffle")

participantsN = int(input("Indica la cantidad de participantes:\n"))

while participantsN <= 0:
    participantsN = int(input("Indica un valor válido para la cantidad de participantes:\n"))

name = ['a' for rep in range(participantsN)]
luckyN = [0 for rep in range(participantsN)]

for rep in range(participantsN):
     name[rep] = input("Indique su nombre: ")
     luckyN[rep] = int(input("Indique su número de la suerte " + name[rep] + ": "))

winnerN = random.randint(1, participantsN)
flag = False
for rep in range(participantsN):
    if luckyN[rep] == winnerN:
        print(f"Felicidades {name[rep]}, ganaste")
        flag = True
if not flag:
    print(f"Nadie ganó, el número ganador fue {winnerN}")



