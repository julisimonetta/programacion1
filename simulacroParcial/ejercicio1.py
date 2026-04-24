"""
Ejercicio 1: Control de vacunación
Crear un programa que:
• Pida la edad de una persona y la cantidad de dosis aplicadas (0, 1 o 2)
• Determine si es menor de edad (<18) o mayor de edad
• Clasifique el estado de vacunación:
o Completo: 2 dosis
o Parcial: 1 dosis
o Sin vacunar: 0 dosis
• Determine acciones:
o Si es menor de edad y tiene 2 dosis: "Apto para actividades escolares"
o Si es mayor de edad y tiene 2 dosis: "Pase sanitario habilitado"
o Si tiene menos de 2 dosis: "Debe completar esquema"
Ejemplo:
Entrada:
20
2
Salida:
Mayor de edad
Estado: Completo
Pase sanitario habilitado
"""


try:
    edad = int(input("Ingrese la edad: "))
    cantDosis = int(input("Ingrese la cantidad de dosis aplicadas: "))

    if edad < 0 or cantDosis < 0:
        print("Por favor ingrese valores validos")
        

except ValueError:
    print("Error al ingresar los datos")

else:
    if cantDosis > 1:
        if edad < 18:
            print("Apto para actividades escolares")
        else:
            print("Pase sanitario habilitado")
    else:
        print("Debe completar esquema")