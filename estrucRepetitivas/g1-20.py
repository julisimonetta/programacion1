"""
Ejercicio 20: Sistema de alquiler de bicicletas
Ingresar la cantidad de horas alquiladas por 25 clientes. Calcular el costo según las horas utilizadas
y aplicar descuentos especiales si el alquiler supera las 5 horas.
"""

for i in range(1, 26, 1):
    costo = 0
    descuento = 0
    cantHoras = float(input(f"Ingrese la cantidad de horas el cliente #{i} alquiló la bicicleta: "))

    costo = cantHoras * 10

    if cantHoras > 5:
        descuento = 10
    
    print(f"El costo del alquiler del cliente #{i} por {cantHoras}h es de ${costo - descuento}")