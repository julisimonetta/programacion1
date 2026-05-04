"""
6. Tarifa de estacionamiento
Cobrar estacionamiento según estas reglas:
• Hasta 2 horas: $1500 por hora.
• Más de 2 y hasta 5 horas: $1200 por hora.
• Más de 5 horas: $1000 por hora.
Si el vehículo es de tipo "moto", tiene 30% de descuento.
Si entra en horario nocturno (después de las 22), tiene además 10% de descuento extra.
Mostrar total a pagar.
"""

try:
    cantHoras = float(input("Ingrese la cantidad de horas en números: "))
    tipoVehiculo = input("Ingrese el tipo de vehiculo (auto/moto): ")
    horario = int(input("Ingrese el horario de entrada en números (24 horas): "))

except ValueError:
    print("Los datos ingresados no son validos")

else:

    if cantHoras < 2:
        precioXHora = 1500
    elif cantHoras >= 2 and cantHoras < 5:
        precioXHora = 1200
    else:
        precioXHora = 1000
    
    estacionamiento = cantHoras * precioXHora

    if tipoVehiculo == "moto":
        descuentoTV = estacionamiento * 0.30

    if horario >= 22: # Horario nocturno
        descuentoH = estacionamiento * 0.10

finally:
    print(f"Estacionamiento: ${estacionamiento}")
    print(f"Descuento por tipo de vehiculo: ${descuentoTV}")
    print(f"Descuento por horario: ${descuentoH}")
    print(f"Total estacionamiento es: {estacionamiento - descuentoTV - descuentoH}")

