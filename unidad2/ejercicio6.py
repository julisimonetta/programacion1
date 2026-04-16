""" 
    Se tiene como datos los sueldos de tres empleados: Suel1, Suel2, Suel3 y tres descuentos
    variables expresados como porcentajes: Porc1, Porc2, Porc3, respectivamente. Calcular
    y mostrar cada uno de los sueldos netos. 
"""

suel1 = float(input("Ingrese el sueldo del primer empleado: ")); """ Tipo Float porque es un sueldo """
suel2 = float(input("Ingrese el sueldo del segundo empleado: ")); """ Tipo Float porque es un sueldo """
suel3 = float(input("Ingrese el sueldo del tercer empleado: ")); """ Tipo Float porque es un sueldo """
porc1 = float(input("Ingrese el porcentaje de descuento para el primer empleado: ")); """ Tipo Float porque es un porcentaje """
porc2 = float(input("Ingrese el porcentaje de descuento para el segundo empleado: ")); """ Tipo Float porque es un porcentaje """
porc3 = float(input("Ingrese el porcentaje de descuento para el tercer empleado: ")); """ Tipo Float porque es un porcentaje """
neto1 = suel1 - ((suel1 * porc1) / 100)
neto2 = suel2 - ((suel2 * porc2) / 100)
neto3 = suel3 - ((suel3 * porc3) / 100)
print("El sueldo neto del primer empleado es:", neto1); """ Tipo Float porque es la resta de un sueldo y un porcentaje (Implicito) """
print("El sueldo neto del segundo empleado es:", neto2); """ Tipo Float porque es la resta de un sueldo y un porcentaje (Implicito) """
print("El sueldo neto del tercer empleado es:", neto3); """ Tipo Float porque es la resta de un sueldo y un porcentaje (Implicito) """