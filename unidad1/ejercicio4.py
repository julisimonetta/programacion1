#Consigna 4:
"""
    Un cine cobra $3500 por entrada. Si una persona compra varias entradas, obtiene un descuento del 20% sobre el total.
    Ingresar la cantidad de entradas y calcular cuanto deberá pagar. 
"""

valorEntrada = 3500
cantidadEntradas = int(input("Ingrese la cantidad de entradas: ")); 
total = cantidadEntradas * valorEntrada; """ Calcular el total sin descuento multiplicando la cantidad de entradas por el valor de cada entrada """
if cantidadEntradas > 2: 
    descuento = total * 0.20
    totalConDescuento = total - descuento; """ Calcular el total a pagar aplicando el descuento del 20% al total """
    print("El total a pagar es: ", totalConDescuento); """ Imprimir el total a pagar por el cliente después de aplicar el descuento """
else:
    total = valorEntrada * cantidadEntradas
    print("El total a pagar es: ", total); """ Imprimir el total a pagar por el cliente sin descuento """
