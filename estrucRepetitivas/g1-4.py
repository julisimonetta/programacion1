"""
Ejercicio 4: Venta de entradas de cine
Ingresar la edad de los clientes hasta que se ingrese una edad negativa. Determinar el precio de la
entrada según la edad y calcular cuántas entradas infantiles, generales y jubilados se vendieron.

infantiles <10 $100
generales $ 500
jubilados > 65 $300
"""
infantil = 0
jubilado = 0
general = 0
edad = int(input("Ingrese su edad en números (negativa para terminar): "))
while (edad > 0):
    if edad < 10:
        infantil += 1
        print("El precio de la entrada es de $100")
    elif edad >= 65:
        jubilado += 1
        print("El precio de la entrada es de $300")
    else:
        general += 1
        print("El precio de la entrada es de $500")
    
    edad = int(input("Ingrese su edad en números (negativa para terminar): "))

print(f"Se vendieron {infantil} entradas infantiles")
print(f"Se vendieron {jubilado} entradas para jubilados")
print(f"Se vendieron {general} entradas generales")