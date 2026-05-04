"""
Ejercicio 2: Torneo de pádel
Ingresar la categoría de 20 jugadores (Primera, Segunda o Tercera). Calcular el costo de
inscripción según la categoría y mostrar el total recaudado y la cantidad de jugadores por categoría.

categoria 1 = 10000 
categoria 2 = 8000
categoria 3 = 5000
"""

jugadores1 = 0
jugadores2 = 0
jugadores3 = 0

for i in range(0, 21, 1):
    cat = int(input("Ingrese su categoría en número (1/2/3): "))
    if cat == 1:
        jugadores1 = jugadores1 + 1
    elif cat == 2:
        jugadores2 = jugadores2 + 1
    elif cat == 3:
        jugadores3 = jugadores3 + 1
    else:
        print("Categoría inválida. Por favor ingrese un valor correcto")

print(f"Hay {jugadores1} de la categoría 'Primera'")
print(f"Hay {jugadores2} de la categoría 'Segunda'")
print(f"Hay {jugadores3} de la categoría 'Tercera'")
total = (jugadores1 * 10000) + (jugadores2 * 8000) + (jugadores3 * 5000)
print(f"El total recaudado es de ${total}")