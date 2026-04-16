#   Consigna 2: 
"""
    Un empleado recibe un sueldo base mensual, además recibe un bono del 15% sobre su sueldo. 
    Si el sueldo base es ingresado por teclado, determinar el sueldo final a cobrar.
"""

sueldoBase = int(input("Ingrese el sueldo base del empleado: ")); """ Ingreso por consola del valor del sueldo base"""
bonoPorcentaje = 0.15; """ Porcentaje del bono (15%)"""
bonoTotal = sueldoBase * bonoPorcentaje; """ Calcular el monto total del bono """
sueldoTotal = sueldoBase + bonoTotal; """ Calcular el sueldo total sumando el sueldo base y el bono total """
print("El sueldo total del empleado es: ", sueldoTotal); """ Imprimir el sueldo total del empleado """