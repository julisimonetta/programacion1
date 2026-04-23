# Consigna 1:
"""
 Un cliente realiza una compra en un supermercado y adquiere 3 productos. El valor del producto 1 es de $4500, 
 el producto 2 es de $3200 y el producto 3 es de $2100. El supermercado ofrece una comisión del 10% sobre el 
 total de la compra. Calcular el total a pagar por el cliente después de aplicar la comisión.
"""

producto1 = int(input("Ingrese el valor del producto 1: ")); """ Valor producto 1"""
producto2 = int(input("Ingrese el valor del producto 2: ")); """ Valor producto 2"""
producto3 = int(input("Ingrese el valor del producto 3: ")); """ Valor producto 3"""

suma = producto1 + producto2 + producto3; """ Suma de los productos"""
comision = (suma / 100) * 10; """ Calcular comisión """
print(suma)
print(comision)
total = suma - comision; """ Calcular total """
print(total); """ Imprimir total """
# Agregar el condicional si los productos tienen importe cero
# Agregar control de excepciones

# voy a crear la rama desarrollo 