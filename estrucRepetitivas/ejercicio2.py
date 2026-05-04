for i in range(2, 100, 1):
    if (i == 2 or i == 3 or i == 5):
        print(f"El numero {i} es primo")
    elif i%2 == 0 or i%3 == 0 or i%5 == 0:
        print(f"El numero {i} no es primo")
    else:
        print(f"El numero {i} es primo")

# Numeros primos (1-100): 
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97 
