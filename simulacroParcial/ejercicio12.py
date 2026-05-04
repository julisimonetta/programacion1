""" 9. Menú de comidas
Mostrar un menú:
1. Hamburguesa
2. Pizza
3. Ensalada
4. Empanadas
Luego pedir bebida:
• agua
• gaseosa
Aplicar reglas:
• Si elige ensalada + agua, descuento del 20%.
• Si elige pizza + gaseosa, recargo del 10%.
• En los demás casos, precio normal.
Mostrar total final.
"""

menHamburguesa = 150
menPizza = 100
menEnsadada = 25
menEmpanadas = 50
menAgua = 75
menGaseosa = 100

try:
    comida = input("Ingrese la opción que desa comer: \n Hamburguesa \n Pizza \n Ensalada \n Empanadas \n")
    bebida = input("Ingrese la opción que desa tomar: \n Agua \n gaseosa \n")

except ValueError:
    print("Los datos ingresados no son válidos")

else: 
    if (comida == "hamburguesa" or comida == "pizza" or comida == "ensalada" or comida == "empanadas") and (bebida == "agua" or bebida == "gaseosa"):
        descuento = 0
        recargo = 0
        
        if comida == "ensada" and bebida == "agua":
            totalSD = menAgua + menEnsadada
            descuento = totalSD * 0.20
            total = totalSD - descuento
        elif comida == "pizza" and bebida == "gaseosa":
            totalSR = menGaseosa + menPizza
            recargo = totalSR * 0.10
            total = totalSR + recargo
        else:
            valorComida = 0
            valorBebida = 0
            match comida:
                case "hamburguesa":
                    valorComida = 150
                case "empanadas":
                    valorComida = 50
                case "ensalada":
                    valorComida = 25
                case  "pizza":
                    valorComida = 100
            match bebida:
                case "agua":
                    valorBebida = 75
                case "gaseosa":
                    valorBebida = 100
            
            total = valorBebida + valorComida
        
        print(f"El total es: ${total}")
        print(f"El recargo es de: ${recargo}")
        print(f"El descuento es de: ${descuento}")
    else:
        print("La opción ingresada no es válida.")