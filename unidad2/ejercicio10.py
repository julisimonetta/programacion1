"""
    La serie numérica de Fibonacci declara que cada término de la misma es la suma de los
    dos términos anteriores. Teniendo como datos el término N1 y el posterior N2, calcular
    y mostrar los 5 términos siguientes. 
"""


"""
N1 = int(input("Ingrese el primer término de la serie de Fibonacci: ")); 
N2 = int(input("Ingrese el segundo término de la serie de Fibonacci: "));
print("Los 5 términos siguientes de la serie de Fibonacci son:")
for i in range(5):
    N3 = N1 + N2;
    print(N3); 
    N1 = N2; 
    N2 = N3; 
"""

f0 = 0
f1 = 1
f2 = f0 + f1
f3 = f1 + f2
f4 = f2 + f3
f5 = f3 + f4
f6 = f4 + f5
print("El primer número es: ", f2);
print("El segundo número es: ", f3);
print("El tercer número es: ", f4);
print("El cuarto número es: ", f5);
print("El quinto número es: ", f6);
