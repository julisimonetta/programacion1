"""
Ejercicio 9: Control de stock de librería
Registrar las ventas diarias de un producto durante 7 días. El stock inicial es de 120 unidades.
Mostrar el stock restante y advertir si en algún momento el stock fue menor a 10 unidades.
"""

stock = 120
for i in range(0,8,1):
    ventas = int(input("Ingrese las ventas diarias del producto: "))

    stock = stock - ventas

    if stock < 10:
        print("Quedan menos de 10 unidades") 
    
    print(f"El stock restante es de {stock}")