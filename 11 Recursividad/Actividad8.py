#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
# y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero,digito):
    if numero == 0:
        return 0
    else:
         ultimoDigito = numero % 10
         if ultimoDigito == digito:
             return 1 + contar_digito(numero // 10,digito)
         else:
             return contar_digito(numero // 10, digito)



print(contar_digito(12233, 3))