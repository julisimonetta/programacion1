"""
Utilizando la estructura condicional multiple. Realice un algoritmo que ingresando un número 
del 0 al 5, muestre un mensaje indicando el mismo numero escrito en letras.

Entrada: 1

Salida: "uno"

"""

num = int(input("Ingrese un número del 1 al 5: "))

match num:
    case 1:
        print("uno")
    case 2:
        print("dos")
    case 3: 
        print("tres")
    case 4:
        print("cuatro")
    case 5:
        print("cinco")
    case _:
        print("El dato ingresado no es valido")