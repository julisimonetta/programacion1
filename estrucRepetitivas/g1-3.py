"""
Ejercicio 3: Consumo eléctrico domiciliario
Ingresar el consumo mensual de energía de 15 viviendas. Aplicar un descuento de 10% si el consumo es 
menor a 250 kWh y un recargo del 15% si supera los 900 kWh. Mostrar el importe final de cada vivenda y
el promedio general
"""

promedio = 0
for i in range(1, 16, 1):
    descuento = 0
    recargo = 0
    consumo = int(input(f"Ingrese el consumo mensual de la vivienda #{i}: "))
    promedio += consumo
    precioXConsumo = 10
    precio = consumo * precioXConsumo
    print("precio", precio)
    if (consumo < 250):
        descuento = precio * 0.10
    elif (consumo > 900):
        recargo = precio * 0.15

    total = (precio + recargo) - descuento
    print("total", total)
    print("recargo", recargo)
    print("descuento", descuento)
    print(f"El importe total es de ${total}")

print(f"El promedio general de consumo en las 15 viviendas fué de: {promedio / 15}")