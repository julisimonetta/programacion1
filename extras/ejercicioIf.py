"""
num = int(input("Ingrese un número: "))

if (num % 2 == 0):
    print("El numero es par")
else: 
    print("El numero es inpar")
"""

# < >

"""
edad = int(input("Ingrese su edad: "))

if (edad < 18):
    print("Sos menor de edad")
elif edad < 28:
    print("Sos estudiante de la UTN")
elif edad < 60:
    print("Sos profesor")
else:
    print("Sos jubilado")

    
if (edad < 18):
    print("Sos menor de edad")
elif ( edad > 18  and edad < 27):
    print("Sos estudiante de la UTN")
elif ( edad > 27  and edad < 60):
    print("Sos profesor")
else:
    print("Sos jubilado")
"""


"""
mes = int(input("Ingrese el número del mes:  "))
match mes:
    case 1:
        print("ENERO")
    case 2:
        print("FEBRERO")
    case 3: 
        print("MARZO") 
    case 4: 
        print("ABRIL")
    case 5: 
        print("MAYO")
    case 6: 
        print("JUNIO")
    case 7:
        print("JULIO")
    case 8:
        print("AGOSTO")
    case 9:
        print("SEPTIEMBRE")
    case 10:
        print("OCTUBRE")
    case 11:
        print("NOVIEMBRE")
    case 12:
        print("DICIEMBRE")
    case _:
        print("No pertenece a ningún mes")
"""

try:
    invitadosCA = int(input("Ingrese la cantidad de invitados: "))
    bebidaCa = int(input("Ingrese el total de la bebida con alcohol"));
    if (invitadosCA > 0):
        extra = bebidaCa / invitadosCA
        print("El importe extra por el consume de alcohol es: ", extra)
    else:
        print("No hay personas que consuman alcohol: ")

except ValueError:
    print("los datos ingresados son erroneos")