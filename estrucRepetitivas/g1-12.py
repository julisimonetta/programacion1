"""
Ejercicio 12: Maratón solidaria
Ingresar la distancia recorrida por 25 participantes. Determinar cuántos superaron los 10 km y
calcular la distancia promedio recorrida.
"""

promedio = 0
mas10k = 0

for i in range(1, 26, 1):
    distancia = float(input(f"Ingrese la distancia recorrida del participante #{i}: "))

    if distancia > 10:
        mas10k += 1

    promedio += distancia
    
promedio = promedio / 25
print(f"El promedio fue de: {promedio}km")
print(f"{mas10k} participantes superaron los 10Km")