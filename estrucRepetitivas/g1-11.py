"""
Ejercicio 11: Sistema de peaje
Registrar el tipo de vehículo de 50 vehículos que pasan por un peaje (auto, moto o camión).
Calcular el monto total recaudado y la cantidad de vehículos por categoría.

auto = 7
moto = 5
camion = 10
"""

cantAutos = 0
cantMotos = 0
cantCamion = 0
total = 0

for i in range(1, 51, 1):
    vehiculo = input("Ingrese el tipo de vehiculo que pasó por el peaje (auto, moto o camión): ")

    if vehiculo == "auto" or vehiculo == "Auto":
        cantAutos += 1
        total += 7
    elif vehiculo == "moto" or vehiculo == "Moto":
        cantMotos += 1
        total += 5
    elif vehiculo == "camion" or vehiculo == "Camion" or vehiculo == "camión" or vehiculo == "Camión":
        cantCamion += 1
        total += 10
    else:
        print("Ingrese un tipo de vehiculo válido.")
    
print(f"El total recaudado fué de: {total}")
print(f"Pasaron {cantAutos} autos por el peaje.")
print(f"Pasaron {cantMotos} motos por el peaje.")
print(f"Pasaron {cantCamion} camiones por el peaje.")