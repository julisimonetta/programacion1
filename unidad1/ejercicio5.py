# Consigna 5
"""
    En un restaurante, el cliente desea dejar una propina del 12% sobre el total consumido. Si el monto total de la
    cuenta es ingresado por teclado, calcular el total a pagar incluyendo la propina.
"""

TotalConsumido = int(input("Ingrese el total consumido por el cliente: "));
propina = TotalConsumido * 0.12;
totalPagar = TotalConsumido + propina;
print("El total a pagar por el cliente es: ", totalPagar);