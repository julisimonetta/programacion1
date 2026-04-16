#Consigna 3:
"""
    Un vehiculo consume cierta cantidad de litros de combustible en un viaje. El precio por litro de nafta es de $980. 
    Si el cliente ingresa la cantidad de litros usados, determinar el total gastado por el cliente en el viaje.
"""

valorPorLitro = 980
litrosUsados = int(input("Ingrese la cantidad de litros usados: ")); """ Ingreso por consola de la cantidad de litros usados """
totalGastado = litrosUsados * valorPorLitro; """ Calcular el total gastado multiplicando la cantidad de litros usados por el valor por litro """
print("El total gastado por el cliente es: ", totalGastado); """ Imprimir el total gastado por el cliente """