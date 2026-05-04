"""
Juego de piedra, papel o tijera
Usuario ingresa opción y la computadora otra (podés simularla).
Determinar:
• empate
• gana usuario
• gana computadora
"""

try:
    usuario = input("Ingrese una opción: \n piedra \n papel \n tijera \n" )
    computadora = "piedra"

except ValueError:
    print("Los datos ingresados no son validos")

else:
    if usuario == "piedra":
        if computadora == "piedra":
            print("Empate")
        elif computadora == "papel":
            print("Gana computadora")
        else: 
            print("Gana usuario")
    elif usuario == "papel":
        if computadora == "papel":
            print("Empate")
        elif computadora == "piedra":
            print("Gana usuario")
        else:
            print("Gana computadora")
    else:  #usuario == tijera
        if computadora == "tijera":
            print("Empate")
        elif computadora == "papel":
            print("Gana usuario")
        else:
            print("Gana Computadora")

finally:
    print(f"Usuario: {usuario}")
    print(f"Computadora: {computadora}")



