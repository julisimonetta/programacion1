"""

Enunciado: 
La empresa de alquiler de vehiculos "Rutas del centro" se dedica a ofrecer autos para uso particular y corporativo. Cuenta
con distintos tipos de vehiculos, como autos compactos, camionetas y utilitarios. Además, brinda servicios adicionales como
GPS, sillas para niños y seguros extendidos, auqnue estos servicios no siempre son contratados por el cliente. 
El proceso de alquiler comienza cuando el cliente se presenta en la sucursal y es atendido por un empleado administrativo,
quien registra sus datos personales, el tipo de vehiculo seleccionado y la cantidad de dias que desea utilizarlo. Tambien se
registran datos adicionales como el color del vehiculo, la patente y el nombre del empleado que realizo la atencion, aunque
estos datos no intervienen en el calculo del costo. 

Cada tipo de vehiculo tiene un precio base por dia, pero en este caso el sistema solo debera considerar el precio diario
ingresado por el usuario y la cantidad de dias de alquiler. No se tendrán en cuenta descuentos, recargos ni impuestos
adicionales.

Se solicita desarrollar un programa que permita ingresar el precio por dia del vehiculo y la cantidad de dias de alquiler,
y luego calcule el costo total del alquiler mostrando el resultado por pantalla.

"""

precioPorDia = float(input("Ingrese el precio por día del vehículo: ")); """ Tipo Float porque es una cantidad de dinero """
cantidadDias = int(input("Ingrese la cantidad de días de alquiler: ")); """ Tipo Int porque es una cantidad de días """
costoTotal = precioPorDia * cantidadDias; """ Tipo Float porque es una cantidad de dinero """
print("El costo total del alquiler es:", costoTotal); """ Tipo Float porque es una cantidad de dinero (Implicito) """