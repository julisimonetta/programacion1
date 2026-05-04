"""
Ejercicio 16: Control de acceso a un recital
Registrar las edades de las personas hasta que se ingrese 0. Informar cuántos son menores de
edad, cuántos mayores y la edad promedio.
"""

mayores = 0
menores = 0
promedio = 0
cantEdades = 0
edad = int(input("Ingrese la edad de la persona (Cero para terminar): "))
while edad > 0:
    if edad >= 18:
        mayores += 1
    else:
        menores += 1
    
    promedio += edad
    cantEdades += 1

    edad = int(input("Ingrese la edad de la persona (Cero para terminar): "))

promedio = promedio / cantEdades
print(f"{mayores} personas son mayores de edad")
print(f"{menores} personas son menores de edad")
print(f"El promedio de edad es: {promedio}")