"""
Identifique si un número N ingresado es primo o no
"""
import math

numPrimo = int(input("Ingrese un número: "))
ultimoDigito = numPrimo % 10

if numPrimo == 2 or numPrimo == 5 or numPrimo == 3:
    print("El primo")
elif numPrimo <= 1:
    print("No es primo")
elif numPrimo%2 == 0 or numPrimo%3 == 0:
    print("No es primo")
elif (ultimoDigito == 5 or ultimoDigito == 0) and numPrimo != 5:
    print("No es primo")
else:
    esPrimo: bool = True
    raiz = math.sqrt(numPrimo)
    for i in (2, raiz):
        if (numPrimo % i == 0):
            esPrimo = False

    if esPrimo:
        print("Es primo")
    else:
        print("No es primo")


# Numeros primos (1-100): 
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97 