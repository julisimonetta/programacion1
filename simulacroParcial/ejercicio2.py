"""
Ejercicio 2: Compra en supermercado
Crear un programa que:
• Pida la edad del cliente y el monto total de compra
• Determine si es menor de edad o mayor de edad
• Clasifique el tipo de compra:
o Alta: >= 10000
o Media: >= 5000
o Baja: < 5000
• Aplique beneficios:
o Si es mayor de edad y compra >= 10000: "Descuento del 15%"
o Si es menor de edad y compra >= 5000: "Descuento del 10%"
o Si compra < 5000: "Sin descuento"
Ejemplo:
Entrada:
35
12000
Salida:
Mayor de edad
Compra: Alta
Descuento del 15%
"""

try:
    edad = int(input("Ingrese la edad: "))
    total = float(input("Ingrese el total de la compra: "))
except ValueError:
    print("Los datos ingresados no son validos")
else:
    if total >= 10000:
        print("Compra: Alta")
        if edad > 17:
            print("Mayor de edad")
            print("Descuento del 15%")
        else:
            print("Menor de edad")
    elif total >= 5000:
        print("Compra: Media")
        if edad <= 17:
            print("Menor de edad")
            print("Descuento del 10%")
        else:
            print("Mayor de edad")
    else:
        if edad > 17:
            print("Mayor de edad")
        else:
            print("Menor de edad")
        print("Comrpa: Baja")
        print("Sin descuento")