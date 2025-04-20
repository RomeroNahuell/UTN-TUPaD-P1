#Ejercicio 1

def hola_mundo():
    print("Hola Mundo!")
#programa_principal
hola_mundo()

#Ejercicio 2

def saludar_usuario(nombre):
    return f"hola {nombre}!"
#programa principal
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en  {residencia}")

#principal

nom= input("ingrese su nombre: ")
apell =input("ingrese su apellido: ")
edad= input("ingrese su edad: ")
residencia =input("ingrese su residencia: ")

informacion_personal(nom, apell, edad, residencia)

#Ejercicio 4
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    return area 

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro
#principal
radio = float(input("ingrese el radio "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"el area del circulo es {area}")
print(f"el perimetro del circulo es {perimetro}")

#Ejercicio 5

def segundos_horas(segundo):
    horas = segundo // 3600
    return horas
#principal

segundos = float(input("ingrese los segundos: "))

horas = segundos_horas(segundos)
print (f"los segundos ingresados en horas son {horas}")

#Ejercicio 6

def tabla_multiplicar(num):
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")

# principal
numero = int(input("Ingrese el número: "))
tabla_multiplicar(numero)

#Ejercicio 7

def operaciones_basicas(a,b):
        suma = a + b
        resta = a - b
        mult = a * b
        div = a / b  if b != 0 else "Indefinido" 
        return (suma, resta, mult, div )

#principal
a = float (input("ingrese un numero: "))
b = float (input("ingrese el segundo numero: "))

resultado = operaciones_basicas (a,b)

print(f"La suma es: {resultado[0]}")
print(f"La resta es: {resultado[1]}")
print(f"La multiplicación es: {resultado[2]}")
print(f"La división es: {resultado[3]}")

#Ejercicio 8

def calcular_imc(peso,altura):
    masaCorporal = peso / altura ** 2
    return masaCorporal
#principal

peso = float(input("ingrese su peso en kg:"))
altura = float(input("ingrese su altura en metros:"))


Imc = calcular_imc( peso ,altura)
print (f"su indice de masa corporal es {Imc: .2f}")

#Ejercicio 9

def celsius_a_fahrenheit(celsius):
    GFahrenheit =  1.8 * celsius + 32
    return GFahrenheit
#principal

Temp = float(input("ingrese una temperatura en grados Celsius:"))
conversion = celsius_a_fahrenheit(Temp)

print(f"el equivalente a grados Fahrenheit es: {conversion}")

#Ejercicio 10

def calcular_promedio(a,b,c):
    promedio = (a + b + c ) / 3
    return promedio
#principal
a = float(input("ingrese el primer numero:"))
b = float(input("ingrese el segundo numero:"))
c = float(input("ingrese el tercer numero:"))

promedio = calcular_promedio(a,b,c)
print (f"el promedio de los numeros dados es de:{promedio}")