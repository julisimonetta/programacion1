"""
Ejercicio 6: Cálculo de sueldo semanal
Ingresar las horas trabajadas de 12 empleados. Si supera las 48 horas semanales, las horas
excedentes se pagan dobles. Mostrar sueldo individual y total abonado por la empresa.
sueldoXHora = 10
sueldoXhoraExtra = 15
"""

totalEmpresa = 0

for i in range(1, 13, 1):
    sueldo = 0
    sueldoXHoraExtra = 0
    sueldoXHora = 0
    sueldoXHora = 0
    cantHoras = int(input("Ingrese la cantidad de horas semanales trabajadas: "))

    if cantHoras > 48:
        horasExtra = cantHoras - 48
        sueldoXHoraExtra = horasExtra * 15
        sueldoXHora = 48 * 10
    else:
        sueldoXHora = cantHoras * 10
    
    sueldo = sueldoXHora + sueldoXHoraExtra
    totalEmpresa += sueldo
    print(f"La cantidad abonada como sueldo es de ${sueldoXHora}")
    print(f"La cantidad abonada por horas extra es de ${sueldoXHoraExtra}")
    print(f"El sueldo es de ${sueldo}")

print(f"El total gastado por la empresa es de ${totalEmpresa}")


