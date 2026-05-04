"""
Ejercicio 14: Tienda de celulares
Registrar las ventas de 20 celulares indicando marca y precio. Aplicar descuentos según la marca y
mostrar el total facturado y la cantidad de equipos vendidos por marca.
"""

totalSamsung = 0
totalXiaomi = 0
totalApple = 0
total = 0

for i in range(1,21,1):
    precioFinal = 0
    precio = 0
    marca = input("Ingrese la marca del celular vendido: ")
    precio = float(input("Ingrese el precio del celular vendido: "))

    if marca == "samsung" or marca == "Samsung":
        totalSamsung += 1
        descuento = 0.20
    elif marca == "xiaomi" or marca == "Xiaomi":
        totalXiaomi += 1
        descuento = 0.25
    elif marca == "apple" or marca == "Apple":
        totalApple += 1
        descuento = 0.05
    else:
        print("No se vende esa marca en este local. Ingrese una marca válida")
    
    descuento = precio * descuento
    precioFinal = precio - descuento
    print(f"El precio final es de ${precioFinal}")
    total += precioFinal

print(f"El total facturado fue de ${total}")
print(f"Se vendieron {totalSamsung} celulares Samsung")
print(f"Se vendieron {totalXiaomi} celulares Xiaomi")
print(f"Se vendieron {totalApple} celulares Apple")