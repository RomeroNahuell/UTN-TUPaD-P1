#Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(n,m):
    if m== 0 :
        return 1
    else:
        return n * potencia(n,m-1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base}^{exponente} = {potencia(base, exponente)}")