numero = input("Ingrese un número entero de tres cifras: ")

if numero == "":
    print("Error al ingresar los datos")

else:
    try:
        numero = int(numero)

        if numero < 0:
            print("El numero debe ser mayor a 0")

        else:
            # Validar que tenga exactamente 3 cifras
            if numero < 100 or numero > 999:
                print("El numero debe ser de 3 cifras")
            else:
                # Obtener cada cifra
                centena = numero // 100
                decena = (numero // 10) % 10
                unidad = numero % 10

                # Verificar si es capicúa
                if centena == unidad:
                    print("Es capicua")
                else:
                    print("No es capicua")

    except:
        print("Error al ingresar los datos")