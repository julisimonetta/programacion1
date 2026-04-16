""" 
 Teniendo como dato un número par N, calcular y mostrar los cinco impares siguientes a él. 
"""

numPar = int(input("Ingrese un número par N: ")); """ Tipo Int porque es un numero par """
if numPar % 2 == 0:
    print("Los cinco números impares siguientes a N son:")
    for i in range(1, 11, 2):
        print(numPar + i); """ Tipo Int porque es un numero impar (Implicito) """
else:
    print("El número ingresado no es par."); """ Tipo texto """


"""
range(inicio, fin, paso)

    inicio = 1 (empieza en 1 (primer número impar))
    fin = 11 (se detiene antes de 11)
    paso = 2 (avanza de 2 en 2)
"""