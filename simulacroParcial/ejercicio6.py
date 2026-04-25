"""
3. Año y mes válidos
Ingresar un mes y un año. Mostrar cuántos días tiene ese mes, teniendo en cuenta si el
año es bisiesto.
"""
try:
    mes = input("Ingrese el mes con el nombre en minusculas: ")
    anio = int(input("Ingrese el año: "))
except ValueError:
    print("Los datos ingresados no son validos")
else:
    if ((mes == "Febrero") or (mes == "febrero")):
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print("El año es biciesto, tiene 29 días")
        else: 
            print("El año no es biciesto")
    else:
        if mes == "Abril" or mes == "abril" or mes == "Junio" or mes == "junio" or mes == "Septiembre" or mes == "septiembre" or mes == "Noviembre" or mes == "noviembre":
            print(f"El mes {mes} del año {anio} tiene 30 días")
        else:
            print(f"El mes {mes} del año {anio} tiene 31 días")