"""
10. Cajero automático
Pedir saldo actual y monto a extraer.
Validar:
• que el monto sea múltiplo de 1000,
• que no supere el saldo,
• y que no sea mayor a $100000 por operación.
Mostrar si la extracción fue aprobada y el saldo restante, o indicar por qué fue
rechazada.
"""

try:
    saldoActual = int(input("Ingrese el saldo actual de su cuenta: "))
    montoAExtraer = int(input("Ingrese el monto a extraer: "))

except ValueError:
    print("Los datos ingresados no son válidos")

else:
    if montoAExtraer % 1000 == 0:
        if montoAExtraer <= saldoActual:
            if montoAExtraer <= 100000:
                print("Extracción aprobada")
                saldoRestante = saldoActual - montoAExtraer
                print(f"Saldo restante en la cuenta = ${saldoRestante}")
            else:
                print("Extracción denegada: No se puede realizar una extracción mayor a 100.000")
        else:
            print("Extracción denegada: No tiene suficiente saldo en tu cuenta para hacer esta operación")
    else:
        print("Extracción denegada: El monto a extraer debe ser multiplo de 1.000")
