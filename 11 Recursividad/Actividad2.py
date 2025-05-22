#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
posicion = int(input("Ingrese la posicion que desea ver: "))

for i in range(0, posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")