"""
7. Compra con cuotas
Ingresar precio y cantidad de cuotas:
• 1 cuota → sin interés
• 3 cuotas → 10% interés
• 6 cuotas → 20% interés
• 12 cuotas → 40% interés
Calcular valor final y valor por cuota.
"""

try: 
    precio = float(input("Ingrese el precio total: "))
    cCuotas = int(input("Ingrese la cantidad de cuotas: (1/3/6/12) "))

except ValueError:
    print("Los datos ingresados no son válidos")

else:
    if cCuotas == 1 or cCuotas == 3 or cCuotas == 6 or cCuotas == 12:
        if cCuotas == 1:
            interes = 0
            valorFinal = precio
            valorPorCuota = precio
        elif cCuotas == 3:
            interes = precio * 0.10
            valorFinal = precio + interes
            valorPorCuota = (valorFinal / 3)
        elif cCuotas == 6:
            interes = precio * 0.20
            valorFinal = precio + interes
            valorPorCuota = (valorFinal / 6)
        else:
            interes = precio * 0.40
            valorFinal = precio + interes
            valorPorCuota = (valorFinal / 12)
        
        print(f"El interes es de: ${interes}")
        print(f"El precio final es de: ${valorFinal}")
        print(f"El valor de cada cuota es de: ${valorPorCuota}")
    
    else:
        print("Los datos ingresados no son validos")