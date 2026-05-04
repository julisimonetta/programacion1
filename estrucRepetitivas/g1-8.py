"""
Ejercicio 8: Competencia de ciclismo
Ingresar los tiempos de 18 corredores. Determinar quién obtuvo el menor tiempo y cuántos
corredores superaron las 2 horas de carrera.
"""

mejorTiempo = 0
masDosHoras = 0
mejorTiempoCorredor = 0
for i in range(1, 19, 1):
    tiempo = float(input(f"Ingresa el tiempo del corredor {i}: "))

    #primer tiempo = mejorTiempo
    if i == 1:
        mejorTiempo = tiempo

    #Calculo mejor tiempo
    if tiempo < mejorTiempo:
        mejorTiempo = tiempo
        mejorTiempoCorredor = i
    
    if tiempo > 2:
        masDosHoras += 1

print(f"El corredor #{mejorTiempoCorredor} fué el corredor con mejor tiempo ({mejorTiempo})")
print(f"{masDosHoras} corredores tuvieron un tiempo de más de dos horas de carrera.")
    

