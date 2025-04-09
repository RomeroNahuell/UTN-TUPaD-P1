#Actividad1 
for num in range(0,101):
    print(num)

#Actividad2
num = int(input("ingrese un numero: ")) 
num = abs (num)
digito = 0

if num == 0:
    digito = 1
else:
    while num > 0:
        num = num // 10
        digito += 1

print(f"el numero tiene {digito} digitos.")

#Actividad3
num1 = int(input("Ingresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))


inicio = min(num1, num2)
fin = max(num1, num2)

sumatoria = 0

for i in range(inicio + 1, fin):
    sumatoria += i
print(f"La suma total de los números comprendidos entre {inicio} y {fin} es: {sumatoria}")


#Actividad4
num = int(input("ingrese un numero: "))
sumatoria = 0


while num != 0:
    sumatoria = sumatoria + num
    num = int(input("ingrese otro numero (0 para terminar): "))
    print()
    
print (f"el total de la suma es {sumatoria}")

#Actividad5
import random
num_Secreto = random.randint(0, 9)
cont = 1
intento = int(input("ingrese numero entre 0 y 9"))
while intento != num_Secreto:
   intento = int(input("Incorrecto, ingrese otro numero"))
   cont += 1
   
print (f"Felicidades adivinaste el numero {intento} en {cont} intentos ")

#Actividad6
for num in range(100,-1,-2):
    print(num)

#Actividad7
num = int(input("ingresa un numero positivo"))
suma = 0

for i in range (1,num):
    suma += i
print(f"la suma entre los numeros 0 y {num} es {suma}")

#Actividad8
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range (1, 101):
    num = int(input("ingrese el primer numero: "))
    if num % 2 == 0:
        pares += 1
    else:
        
        impares +=1
    if num < 0:
        negativos += 1
    else:
        positivos += 1
print(f"los numeros pares son {pares}, los impares {impares}, los positivos {positivos} y los negativos {negativos}.")

#Actividad9
suma = 0
media = 0
cantidad = 100

for i in range (cantidad):
    num = int(input("ingrese un numero: "))
    suma = suma + num
   
media = suma / 100
print (f"la media es {media} ")

#Actividad10
num = int(input("ingrese un numero: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print (f"invertido es {invertido}: ")