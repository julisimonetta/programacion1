try:
    peso = int(input("Ingrese el peso con numeros: "))
    destino = input("El destino es el interior? (s/n): ")
    cliente = input("El cliente es primium? (s/n): ")

except ValueError:
    print("Ls datos ingresados no son validos")

else:
    if (peso < 0) or (destino != "s" and destino != "n") or (cliente != "s" and cliente != "n"):
        print("Los datos ingresados no son válidos")
    else:
        #calculo total del peso
        if peso <= 5:
            tPeso = 2000
        elif peso > 5 and peso <= 20:
            tPeso = 5000
        else:
            tPeso = 10000
        
        #calculo del recargo (destino)
        if destino == "s": #cliente del interior
            recargo = tPeso * 0.15
        
        #calculo descuento (cliente)
        if cliente == "s": #cliente premium
            descuento = tPeso * 0.20
        
        total = (tPeso + recargo) - descuento
        print(f"El envío es: ${tPeso}")
        print(f"El descuento es: ${descuento}")
        print(f"El recargo es: {recargo}")
        print(f"El total es: ${total}")