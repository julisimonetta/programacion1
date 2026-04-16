"""
    Dados cuatro números naturales A, B, C y D, escriba un algoritmo que muestre el
    promedio obtenido 
"""

numA = int(input("Ingrese el primer número: ")); """ Tipo Int porque es un numero natural """
numB = int(input("Ingrese el segundo número: ")); """ Tipo Int porque es un numero natural """
numC = int(input("Ingrese el tercer número: ")); """ Tipo Int porque es un numero natural """
numD = int(input("Ingrese el cuarto número: ")); """ Tipo Int porque es un numero natural """
prom = (numA + numB + numC + numD) / 4
print("El promedio de los cuatro números es:", prom); """ Tipo Float porque es la division de un numero natural (Implicito) """