"""
4. Sueldo con bonificación
Una empresa paga una bonificación según antigüedad y sueldo:
• Si tiene más de 10 años de antigüedad, bono del 10%.
• Si no, pero tiene más de 5 años, bono del 7%.
• Si no, bono del 5%.
Además, si el sueldo es menor a $500000, se agrega un extra del 3%.
Mostrar sueldo final.
"""

antiguedad = float(input("Ingrese su antiguedad: "))
sueldo = float(input("Ingrese su sueldo: "))

if antiguedad > 10:
    bonoAnt = sueldo * 0.10
elif antiguedad > 5 and antiguedad <= 10:
    bonoAnt = sueldo * 0.07
else:
    bonoAnt = sueldo * 0.05

if sueldo < 500000:
    bonoSueldo = sueldo * 0.03

total = sueldo + bonoAnt + bonoSueldo
print(f"El total es {total}")
    