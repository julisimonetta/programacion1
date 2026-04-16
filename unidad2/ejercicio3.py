"""
Sean N y M dos números naturales, escriba un algoritmo para determinar si N es
divisible por M 
"""

numN = int(input("Ingrese el número N: ")); """ Tipo Int porque es un numero natural """
numM = int(input("Ingrese el número M: ")); """ Tipo Int porque es un numero natural """
division = numN % numM
if division == 0:
    print("El número N es divisible por M."); """ Tipo texto """
else:
    print("El número N no es divisible por M."); """ Tipo texto """
