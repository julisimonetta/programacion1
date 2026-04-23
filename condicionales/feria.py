"""
Una nueva feria llega a la ciudad. Los precios varían según la edad:
- Menores de 4 años pasan gratis
- Menores de 12 pagan 1/3 de tarifa
- Menores de 18 pagan media tarifa
- Adultos hasta 60 años pagan tarifa completa
- Adultos mayores y jubilados pagan media tarifa.

Realice un programa donde se ingrese la edad de la persona y como salida indique el monto 
anteponiendo el signo $ y un espacio. Ejemplo para un adulto: $ 150.0
"""

edad = int(input("Ingrese su edad: "))
if (edad < 4):
    print("$ 0.0")
elif (edad >= 4 and edad < 12):
    print("$ 50.0")
elif (edad >= 12 and edad < 18):
    print("$ 75.0")
elif (edad >= 18 and edad < 60):
    print("$ 150.0")
else:
    print("$ 75.0")