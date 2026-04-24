"""
Ejercicio 3: Evaluación de asistencia
Crear un programa que:
• Pida la edad de un alumno y su porcentaje de asistencia (0 a 100)
• Determine si es menor de edad o mayor de edad
• Clasifique la asistencia:
o Excelente: >= 90
o Buena: >= 75
o Regular: >= 60
o Baja: < 60
• Determine condición:
o Si es menor de edad y asistencia >= 75: "Regulariza la materia"
o Si es mayor de edad y asistencia >= 90: "Promoción directa"
o Si asistencia < 60: "Libre por inasistencias"
Ejemplo:
Entrada:
17
80
Salida:
Menor de edad
Asistencia: Buena
Regulariza la materia
"""

try:
    edad = int(input("Ingrese la edad: "))
    asistencia = int(input("Ingrese el promedio de asistencia: "))
except ValueError:
    print("Los datos ingresados no son validos")
else:
    if edad < 18:
        print("Menor de edad")
    else:
        print("Mayor de edad")

    if asistencia < 60:
        print("Asistencia: Baja")
        print("Libre por inasistencias")
    elif asistencia >= 60 and asistencia < 74 :
        print("Asistencia: Regular")
    elif asistencia >= 75 and asistencia <= 89:
        print("Asistencia: Buena")
        if edad < 18:
            print("Regulariza la materia")
    else:
        print("Asistencia: Excelente")
        if edad >= 18:
            print("Libre por inasistencias")