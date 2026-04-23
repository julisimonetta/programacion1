numero = input("Ingrese un número entero de tres cifras: ")
numInt = int(numero)
# validar que tenga valor
if numero == "":
    print("Error al ingresar los datos")
# validar que sea positivo
elif numInt < 0:
    print("El numero debe ser mayor a 0")
# Validar que tenga exactamente 3 cifras
elif (numInt < 99) or (numInt > 1000) :
    print("El numero debe ser de 3 cifras")
else:
    try:
        tercerNum = numInt % 10
        segundoNum = (numInt // 10) % 10
        primerNum = numInt // 100
        print(tercerNum)
        print(segundoNum)
        print(primerNum)

        # Verificar si es capicúa
        if tercerNum == primerNum:
            print("Es capicua")
        else:
            print("No es capicua")
    except:
        print("Error al ingresar los datos")
    finally:
        print("Gracias por usar mi sistema :D")