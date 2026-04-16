#Consigna 9
"""
    Una tienda vende camisetas a $800 cada una. Si el cliente compra más de 5, obtiene un descuento del 25% sobre el
    total. Ingresar la cantidad de camisetas y calcular el monto final.
"""

valorCamisetas = 8000
cantidadCamisetas = int(input("Ingrese la cantidad de camisetas a comprar: "));
total = cantidadCamisetas * valorCamisetas;
if cantidadCamisetas > 5:
    descuento = (total / 100) * 25;
    totalConDescuento = total - descuento; 
    print("El cliente pagará: ", totalConDescuento);
else:
    print("El cliente pagará: ", total);