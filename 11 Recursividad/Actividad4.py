#Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
num = int(input("ingrese un numero: "))

if num == 0:
    print("0")
else:
    print(decimal_a_binario(num))