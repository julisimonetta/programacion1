"""
Teniendo como dato el tiempo transcurrido desde el inicio hasta el final de un acontecimiento
cualquiera expresado en días, hacer los cálculos necesarios e imprimirlo en MINUTOS.
"""

tiempoD = float(input("Ingrese la cantidad de tiempo en días: "))
tiempoM = (tiempoD  * 24) * 60
print(int(tiempoM))