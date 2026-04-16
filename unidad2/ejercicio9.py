"""
    Tres personas deciden invertir su dinero para formar una empresa. Cada una de ellas
    invierte una cantidad distinta. Calcular y mostrar el porcentaje que cada una invierte con
    respecto al total de la inversión. 
"""

persona1 = int(input("ingrese la inversión de la primera persona: "))
persona2 = int(input("Ingrese la inversión de la segunda persona: "))
persona3 = int(input("Ingrese la inversión de la tercera persona: "))
total = persona1 + persona2 + persona3
inversion1 = (total / persona1) * 100
inversion2 = (total / persona2) * 100
inversion3 = (total / persona3) * 100
print("El total es: ", total)
print("La persona 1 invirtió", persona1, "Que corresponde al ", inversion1, "%")
print("La persona 2 invirtió", persona2, "Que corresponde al ", inversion2, "%")
print("La persona 3 invirtió", persona3, "Que corresponde al ", inversion3, "%")


















"""
inversion1 = float(input("Ingrese la inversión de la primera persona: ")); 
inversion2 = float(input("Ingrese la inversión de la segunda persona: ")); 
inversion3 = float(input("Ingrese la inversión de la tercera persona: ")); 
total_inversion = inversion1 + inversion2 + inversion3
porcentaje1 = (inversion1 / total_inversion) * 100
porcentaje2 = (inversion2 / total_inversion) * 100
porcentaje3 = (inversion3 / total_inversion) * 100
print("El porcentaje de inversión de la primera persona es:", porcentaje1, "%"); 
print("El porcentaje de inversión de la segunda persona es:", porcentaje2, "%"); 
print("El porcentaje de inversión de la tercera persona es:", porcentaje3, "%"); 
"""