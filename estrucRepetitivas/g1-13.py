"""
Ejercicio 13: Control de combustible
Ingresar la cantidad de litros cargados por 40 vehículos en una estación de servicio. Informar
cuántos vehículos cargaron más de 40 litros y el total de litros vendidos.

$10 x litro
"""
total = 0
mas40l = 0
for i in range(1, 41, 1):
    litros = float(input(f"Ingrese la cantidad de litros cargados por el vehiculo #{i}: "))
        
    if litros > 40:
        mas40l += 1

    total += litros
    print(total)

print(f"El total de litros vendidos fué de: {total}L")
print(f"{mas40l} vehiculos cargaron más de 40L")