"""
Ejercicio 10: Encuesta de satisfacción
Ingresar la puntuación otorgada por clientes de un restaurante (1 a 5). Finalizar el ingreso cuando
se ingrese 0. Mostrar porcentaje de cada puntuación y promedio general.
"""

puntuacion = int(input("Ingrese su puntuación del restaurante (Cero para terminar): "))
promedio = 0
cantPuntuacion = 0

while puntuacion > 0:
    print(f"La puntuación fue de: {puntuacion}")
    promedio += puntuacion
    cantPuntuacion += 1

    puntuacion = int(input("Ingrese su puntuación del restaurante (Cero para terminar): "))

promedio = promedio / cantPuntuacion
print(f"El promedio general fue de: {promedio}")