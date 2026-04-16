"""
Los chicos del último año de una de las escuelas secundarias del pueblo están organizando una
fiesta y necesitan determinar el importe que debe abonar cada invitado para cubrir los gastos. Sin
embargo, enfrentan un problema: no tienen un sistema eficiente para calcular esta cantidad de
manera justa y precisa, ni tampoco para mostrar cuánto deben pagar por la comida y la bebida sin
alcohol. La situación se complica aún más debido a la falta de un registro claro de los gastos y la
necesidad de mostrar el costo extra que deberá abonar cualquier invitado que consuma bebidas
alcohólicas.
Hay diferentes elementos a considerar: el total gastado en comida, la cantidad exacta de invitados
que asistirán a la cena, el gasto total en bebidas sin alcohol, el gasto en bebidas con alcohol y la
cantidad de invitados que consumieron bebidas alcohólicas.
"""

try:
    gastoTotalComida = float(input("Ingrese el gasto total de la comida: "))
    cantidadInvidatos = int(input("Ingrese la cantidad de invitados: "))
    gastoBebidasSinAlcohol = float(input("Ingrese el gasto total de bebidas sin alcohol: "))
    gastoBebidasConAlcohol = float(input("Ingrese el gasto total de bebidas con alcohol: "))
    invitadosAlcohol = int(input("Ingrese la cant. de personas que consumieron de bebidas con alcohol: "))
    gastoAlcohol = gastoBebidasConAlcohol / invitadosAlcohol
except ValueError:
    print("Error en el ingreso de datos")
else:
    gastoBase = (gastoTotalComida + gastoBebidasSinAlcohol) / cantidadInvidatos
    gastoExtraAlcohol = int(gastoBase + gastoBebidasConAlcohol / invitadosAlcohol)
    print("El gasto base es: ", gastoBase)
    print("Si consumiste alcohol deberás pagar $", gastoExtraAlcohol, " extras")
finally:
    print("Gracias por usar mi programa :D")