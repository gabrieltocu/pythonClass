# Initialize counters
yes_count = 0
no_count = 0
gente = True

# While Loop
while (gente == True):
    response = input("¿Te gustó la conferencia? (si/no): ").lower()

    if response == 'si':
        yes_count += 1
    elif response == 'no':
        no_count += 1
    else:
        print("Indica una respuesta válida. 'si' o 'no'.")

    another_response = input("¿Alguien falta por responder? (si/no): ").lower()
    if another_response == 'si':
        gente = True
    elif another_response == 'no':
        gente = False

total_responses = yes_count + no_count

# Calculate percentages
yes_percentage = (yes_count / total_responses) * 100
no_percentage = (no_count / total_responses) * 100

print(f"\nTotal de gente que le gustó la conferencia: {yes_percentage:.2f}%")
print(f"Total de gente que no le gustó la conferencia: {no_percentage:.2f}%")