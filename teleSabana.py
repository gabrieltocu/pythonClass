# Tiempo en minutos
tiempoMin = 0
# Costo en minutos
costoMin = 0
# Impuesto
impuesto = 0

# Dar bienvenida
print("Bienvenido al simulador de teleSabana")

# Preguntar por el día de la semana en que se hizo la llamada y calcular
diaSemana = input("Dime el día de la semana en que se hizo la llamada: ")

if diaSemana.lower() == "martes":
    impuesto = 0.16
elif diaSemana.lower() == "miercoles":
    impuesto = 0.14
else:
    impuesto = 0.19

# Preguntar el tiempo en minutos
tiempoMin = float(input("Dime en minutos, el tiempo de la llamada: "))

if tiempoMin < 5:
    costoMin = 1000
elif tiempoMin >= 5 and tiempoMin < 8:
    costoMin = 800
elif tiempoMin >= 8 and tiempoMin < 10:
    costoMin = 600
else:
    costoMin = 500

# Calcular el precio de la llamda sin impuestos
resultado = tiempoMin * costoMin
# Calcular el impuesto
imp = resultado * impuesto
# Sumar para dar el precio total de la llamada
precioLlamada = resultado + imp
# Imprimir
print(f"El precio total de su llamada sería de ${precioLlamada} pesos")
