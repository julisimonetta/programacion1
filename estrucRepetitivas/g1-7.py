"""
Ejercicio 7: Estación meteorológica
Cargar la cantidad de lluvia caída durante 30 días. Mostrar el día con mayor lluvia, el promedio
mensual y cuántos días no llovió.
"""

promedio = 0
mayorLluvia = 0
sinLluvia = 0

for i in range(1, 31, 1):
    cantLluvia = float(input(f"Ingrese la cantidad de lluvía durante el día #{i}: "))

    # Si es la primera ronda, se asigna a mayorLluvia
    if i == 1:
        mayorLluvia = cantLluvia
    if cantLluvia > mayorLluvia:
        mayorLluvia = cantLluvia
    
    if cantLluvia == 0:
        sinLluvia += 1

    promedio += cantLluvia

#Calculo promedio:
promedio = promedio / 30
print(f"El promedio de los 30 días es de: {promedio}")

print(f"No llovió por {sinLluvia} días")
print(f"El día con mayor lluvia fué de: {mayorLluvia} ")
