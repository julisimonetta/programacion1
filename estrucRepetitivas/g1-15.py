"""
Ejercicio 15: Examen de manejo
Ingresar el puntaje obtenido por 35 aspirantes. Si el puntaje es mayor o igual a 70, el aspirante
aprueba. Informar cantidad de aprobados, desaprobados y promedio de puntajes.
"""
aprobados = 0
desaprobados = 0
promedio = 0
for i in range(1, 36,1):
    nota = float(input(f"Ingrese la nota del aspirante #{i}: "))

    if nota >= 70:
        aprobados += 1
    else: 
        desaprobados += 1
    
    promedio += nota

promedio = promedio / 35
print(f"La cantidad de desaprobados fué de: {desaprobados}")
print(f"La cantidad de aprobados fué de: {aprobados}")
print(f"El promedio de los puntajes fué de: {promedio}")