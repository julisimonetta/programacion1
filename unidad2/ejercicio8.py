"""
    Dado un número natural N, se quiere obtener un número real R que sea el resultado de
    dividir la suma de los dígitos de N por la cantidad de dígitos que posee N. Por ejemplo:
    Si N = 3421 luego R = 10/4 = 2.5 
"""
"""
numN = input("Ingrese un número natural: ");
suma = 0
cantidad_digitos = len(numN);
for digito in numN:
    suma += int(digito); 
    R = suma / cantidad_digitos
print("El resultado R es:", R); 
"""

"""
numN = input("Ingrese un número de 7 digitos: ")
num0 = int(numN[0])
num1 = int(numN[1])
num2 = int(numN[2])
num3 = int(numN[3])
num4 = int(numN[4])
num5 = int(numN[5])
num6 = int(numN[6])

sumaTotal = num0 + num1 + num2 + num3 + num4 + num5 + num6
print(sumaTotal)
resultado = sumaTotal / 7
print("El numero real que es el resultado es: ", resultado)
"""


n = 8324
d5 = n % 10 
print(d5)
d4 =(n // 10) % 10
print(d4)
d3 = (n // 100 ) % 10
print(d3)
d2 = (n // 1000) % 10
print(d2)
suma = d5 + d4 + d3 + d2
print("La suma es:", suma)

"""
n = input("Ingrese un número: ")
nn = int(n)
d0 =  nn % 10
suma = d0
intento = 1
for numero in n:
    intento = intento * 10
    d = (nn // intento) % 10;
    suma += d
print("suma:", suma)
"""