"""
Utilizando la estructura condicional doble. Realice un algoritmo que ingresando un número, 
muestre un mensaje indicando si el número es par o es impar.

Entrada: un número.

Salida: "Es par" o "Es impar".

"""

num = int(input("Ingrese un número: "))
resto = num % 2
if resto == 0: 
    print("Es par")
else: 
    print("Es impar")