"""
Ejercicio 1: Control de temperatura en un invernadero
Ingresar la temperatura registrada cada hora durante 24 horas. Informar cuántas mediciones
estuvieron por debajo de 10°C, cuántas superaron los 30°C y calcular el promedio general.
"""
sumaTemp = 0
for i in range(0, 25, 1):
    temp = int(input(f"Ingrese la tempratura de la hora {i}: "))
    if temp < 10:
        print(f"la temperatura de la hora {i} fué menor a 10°C ({temp}°C)")
    elif temp > 30:
        print(f"la temperatura de la hora {i} fué mayor a 30°C ({temp}°C)")
    else: 
        print(f"La temperatura de la hora {i} fué de {temp}°C")
    sumaTemp = sumaTemp + temp

promedio = sumaTemp / 24
print(f"El promedio del día fué de: {promedio}°C")
