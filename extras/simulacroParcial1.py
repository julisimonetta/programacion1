"""
    Se solicita desarrollar un programa que permita ingresar el precio por día del vehiculo y la cantidad de dias de alquiler, y 
    luego calcule el costo total del alquiler mostrando el resultado por pantalla
"""

vehiculo = input("Ingrese el nombre del vehículo: "); """ Tipo String porque es el nombre del vehículo """
print("Ingrese el precio por día del alquiler del", vehiculo, ":")
precio_por_dia = float(input()); """ Tipo Float porque es una cantidad de dinero """
cantidad_dias = int(input("Ingrese la cantidad de días de alquiler: ")); """ Tipo Int porque es una cantidad de días """
costo_total = precio_por_dia * cantidad_dias; """ Tipo Float porque es una cantidad de dinero """
print("El costo total del alquiler del", vehiculo, "es:", costo_total); """ Tipo Float porque es una cantidad de dinero (Implicito) """