"""
8. Fecha válida
Ingresar día, mes y año, y determinar si la fecha es válida.
Tener en cuenta:
• meses de 30 días,
• meses de 31 días,
• febrero con 28 o 29 según corresponda.
"""

try:
    dia = int(input("Ingrese el día: "))
    mes = input("Ingrese el més: ")
    anio = int(input("Ingrese el año en números (2026): "))

except ValueError:
    print("Los datos ingresados no son válidos")

else:
    
    if anio > 1926 and anio <= 2026: # validamos fechas entre 1926 y 2026
        if mes == "febrero" or mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre": #meses con 30 o menos días
            if mes == "febrero":
                if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                    if dia >= 1 and dia <= 29:
                        print("La fecha es válida")
                    else:
                        print("La fecha no es válida")
                else: 
                    if dia >= 1 and dia <= 28:
                        print("La fecha es válida")
                    else:
                        print("La fecha no es válida")
            else:
                if dia >= 1 and dia <= 30:
                    print("La fecha es válida")
                else:
                    print("La fecha no es válida")
        else: # meses con 31 días
            if dia >= 1 and dia <= 31:
                print("La fecha es válida")
            else:
                print("La fecha no es válida")
    else:
        print("Por favor, ingrese un año válido.")