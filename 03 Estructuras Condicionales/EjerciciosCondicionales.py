#Ejercicio1
edad = int(input("Ingres su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#Ejercicio2
nota = int(input("Ingres su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio3
NumPar = int(input("Ingrese un Numero Par: "))

if NumPar%2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio4
Edad = int(input("Ingrese su edad: "))

if Edad < 0:
    print("no es posible")
elif Edad < 12:
    print("usted pertenece a la categoria Niño/a")
elif Edad < 18:
    print("Usted pertenece a la categoria Adolescente")
elif Edad < 30:
    print("Usted pertenece a la categoria Adulto/a joven")
else:
    print("Usted pertenece a la categoria Adulto/a")

#Ejercicio5
Contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if len(Contraseña) >=8 and len(Contraseña) <=14 :
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor,ingrese una contraseña entre 8 y 14 caracteres .")

#Ejercicio6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint (1, 100)for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana > moda:
    print("sesgo positivo")
elif media < mediana < moda:
    print("sesgo negativo")
else:
    print("no hay sesgo")

#Ejercicio7
frase = input("Ingrese una frase: ")
vocales = {'a', 'e', 'i', 'o', 'u'}

if frase:
    ultima_letra = frase [-1].lower()  
    if ultima_letra in vocales:
         print(f"{frase}!")
    else:
        print(f"{frase}")
else:
    print("no se registro ninguna frase.")

#Ejercicio8
nombre = input("Ingrese su nombre: ")
num = int(input("seleccione una opcion. 1-Si quiere su numbre en mayusculas. 2-si quiere su nombre en minusculas. 3-si quiere su nombre con la primera letra mayuscula: "))
if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
else:
    print("Opciones no validas")

#Ejercicio9
Magnitud = float(input("Ingrese la magnitud de un terremoto: "))
print("segun la escala de ritcher:")
if Magnitud < 3:
    print("Muy leve")
elif Magnitud >= 3 and Magnitud < 4:
    print("Leve")
elif Magnitud >=4 and Magnitud < 5:
    print("Moderado")
elif Magnitud >=5 and Magnitud < 6:
    print("Fuerte")
elif Magnitud >=6 and Magnitud < 7:
    print("Muy Fuerte")
elif Magnitud  >=  7:
    print("Extremo")

#Ejercicio10

hemisferio = input("¿En cuál hemisferio se encuentra? (Norte/Sur): ").strip().lower()
mes = input("¿En qué mes se encuentra? ").strip().lower()
dia = int(input("¿En qué día se encuentra? "))

# Validar que el mes ingresado sea correcto
meses_validos = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio", 
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

if mes not in meses_validos:
    print("Mes no válido. Por favor, ingrese un mes correcto.")
else:
    # Determinar la estación según el hemisferio
    if hemisferio == "norte":
        if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
            estacion = "Invierno"
        elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
            estacion = "Primavera"
        elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    
    elif hemisferio == "sur":
        if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
            estacion = "Verano"
        elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
            estacion = "Otoño"
        elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    
    else:
        estacion = "Hemisferio no válido. Debe ser 'Norte' o 'Sur'."

    print(f"La estación en la que se encuentra es: {estacion}")