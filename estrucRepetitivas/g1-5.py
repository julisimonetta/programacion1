"""
Ejercicio 5: Control de notas universitarias
Ingresar las notas de 30 alumnos. Informar cantidad de aprobados, desaprobados, promedio del
curso y nota más alta.
"""

desaprobados = 0
aprobados = 0
acu = 0
promedio = 0
notaMasAlta = 0

for i in range(1, 31, 1):
    nota = float(input(f"Ingrese la nota del alumno {i}: "))

    if nota > 10 or nota < 1:
        print("Ingrese una nota válida.")
    else:
        # Acumulador para promedio
        acu += nota

        # Primer nota == nota más alta
        if i == 1:
            notaMasAlta = nota

        # Clasificación aprobados - desaprobados
        if nota < 6:
            desaprobados += 1
        else:
            aprobados += 1

        # Calculo nota mas alta
        if nota > notaMasAlta:
            notaMasAlta = nota
    
print(f"La nota más alta fué: {notaMasAlta}")
print(f"Los desaprobados fueron: {desaprobados}")
print(f"Los aprobados fueron: {aprobados}")
promedio = acu / 30
print(f"El promedio del curso es de: {promedio}")