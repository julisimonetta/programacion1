"""
2. Sistema de envío
Costo de envío según:
• Peso:
o ≤5 kg → $2000
o ≤20 kg → $5000
o 20 kg → $10000
• Si el destino es "interior", recargo del 15%.
• Si el cliente es "premium", descuento del 20% sobre el total final.
"""

try:
    peso = int(input("Ingrese el peso del producto como número: "))
    destino = input("Es un cliente del interior ? (s/n): ")
    cliente = input("Es cliente premium ? (s/n): ")
    costo = 0

    if destino == "":
        print("El destino ingresado no es válido")
    elif cliente == "":
        print("El cliente ingresado no es válido")
    elif peso == 0 or peso < 0:
        print("El peso ingresado no es válido")

except ValueError:
    print("Los datos ingresados no son válidos")

else:
    if peso >= 20:
        costo = 10000
    elif peso < 20 and peso > 5:
        costo = 5000
    else:
        costo = 2000

    if destino == "s":
        extra  = costo * 0.15
        costo += costo + extra
    
    if cliente == "s":
        descuento = costo * 0.20
        costo = costo - descuento

finally:
    print(f"El costo total es: {costo}")



