"""
Ejercicio 19: Control de velocidad
Ingresar la velocidad de 60 vehículos detectados por un radar. Informar cuántos excedieron el límite
permitido de 80 km/h y cuál fue la velocidad máxima registrada.
"""

velocidadMaxima = 0
excedioLimite = 0
for i in range(1, 61, 1):
    velocidad = int(input(f"Ingrese la velocidad detectada del vehiculo #{i}: "))

    # calculo velocidad maxima
    if i == 1:
        velocidadMaxima = velocidad
    if velocidad > velocidadMaxima:
        velocidadMaxima = velocidad

    # Limite velocidad
    if velocidad > 80:
        excedioLimite += 1

print(f"{excedioLimite} vehiculos exedieron el limite de velocidad")
print(f"La velocidad máxima registrada fué de: {velocidadMaxima}")
    



