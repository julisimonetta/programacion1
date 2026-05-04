try:
    acu = 0
    for i in range(0, 5, 1):
        edad = int(input("Ingrese la edad: "))
        acu = acu + edad

except ValueError:
    print("Debes ingresar un dato valido")

else: 
    promedio = acu/5
    print(promedio)
    if promedio >= 18 and promedio < 20:
        print("Enunciado 1")
    elif promedio >= 20 and promedio < 30:
        print("Enunciado 2")
    else:
        print("Enunciado 3")