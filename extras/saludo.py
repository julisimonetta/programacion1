#TARGETA DE CUMPLEAÑOS 1
"""
nombre= input("Ingrese su nombre: ")
print(f"Feliz cumpleaños {nombre} \n que los cumplas feliz!! ❤️")
"""

#TARGETA DE CUMPLEAÑOS 2
"""
print("Hola! Este es un ejemplo en Python")
print("Por favor ingrese su nombre: ")

nombre = input()

print("Bienvenido al sistema ", nombre, ". Gracias por usar mi programa.", sep="")
"""

#TARGETA DE CUMPLEAÑOS 3
"""
cumpleañero = input("Ingrese el nombre del cumpleañero: ")
print("Feliz cumpleaños",cumpleañero,"que los cumplas feliz!! ❤️", sep="/")

"""

# EJEMPLOS DE SEP
"""
cumpleañero = input("Ingrese el nombre del cumpleañero: ")
print("Feliz cumpleaños",cumpleañero,"que los cumplas feliz!! ❤️", sep="/")

sep="/"
sep="."
sep="-"
sep=","
sep="_"
sep="*"
sep="$"

"""



"""
Enunciado entrada al museo:

cantidad = input("Ingrese la cantidad de dinero a gastar: ")
print("La cantidad de personas que pueden entrar es:", (int(cantidad) - 200)/45)
"""

#Enunciado comision de cheques

"""
CALCULANDO DE A UN CHEQUE
cantidad1 = input("Ingrese la cantidad del cheque: ")
comision = (int(cantidad1) / 100) * 3
print("La comision a pagar es:", comision)
"""

cheque1 = int(input("Ingrese la cantidad del cheque 1: "))
cheque2 = int(input("Ingrese la cantidad del cheque 2: "))  
cheque3 = int(input("Ingrese la cantidad del cheque 3: "))
total_cheques = cheque1 + cheque2 + cheque3
comision_total = (total_cheques / 100) * 3
cantAPagar = total_cheques - comision_total
print("El cadete recibira", cantAPagar)