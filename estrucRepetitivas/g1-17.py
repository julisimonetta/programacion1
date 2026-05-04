"""
Ejercicio 17: Producción agrícola
Ingresar la cantidad de kilos cosechados por 10 campos durante una semana. Mostrar cuál obtuvo
la mayor producción y el total cosechado.
"""
campoMayorProduccion = 0
mayorProduccion = 0
total = 0
for i in range(1, 11, 1):
    kilosCosechados = float(input(f"Ingresa la cantidad de kilos cosechados en el campo #{i}: "))

    #primero = mayorProduccion
    if i == 1:
        mayorProduccion = kilosCosechados

    if kilosCosechados > mayorProduccion:
        mayorProduccion = kilosCosechados
        campoMayorProduccion = i
    
    total += kilosCosechados

print(f"El total cosechado fue de: {total}k")
print(f"El campo con mayor producción fue el número {campoMayorProduccion} con {mayorProduccion}k")
    
