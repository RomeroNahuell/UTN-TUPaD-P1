#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    def es_palindromo_rec(palabra, inicio, fin):
        if inicio >= fin:
            return True
        if palabra[inicio] != palabra[fin]:
            return False
        return es_palindromo_rec(palabra, inicio + 1, fin - 1)
    
    palabra = palabra.lower()
    return es_palindromo_rec(palabra, 0, len(palabra) - 1)


texto = input("Ingresa una palabra sin espacios ni tildes: ")
if es_palindromo(texto):
    print("Es palíndromo")
else:
    print("No es palíndromo")