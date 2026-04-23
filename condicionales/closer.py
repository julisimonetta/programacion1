"""
Tres amigos juegan al juego de "Closer", donde el primero de ellos indica un numero entero 
positivo y los otros dos realizan su adivinanza. El algoritmo debe poder decir "Ganador 
Jugador 1" o "Ganador Jugador 2" según quién estuvo más cerca del número original del primer 
amigo.
"""


numero = int(input())
jugador1 = int(input())
jugador2 = int(input())

dif1 = numero - jugador1
if dif1 < 0:
    dif1 = -dif1

dif2 = numero - jugador2
if dif2 < 0:
    dif2 = -dif2

if dif1 < dif2:
    print("Ganador Jugador 1")
elif dif2 < dif1:
    print("Ganador Jugador 2")