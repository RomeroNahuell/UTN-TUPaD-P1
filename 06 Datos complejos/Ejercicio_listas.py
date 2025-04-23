#Ejercicio1
lista_range = list  (range(4,101,4))
print(lista_range)

#Ejercicio2
elementos = [ "plato", "tenedor", "cuchara", "vaso", "cuchillo" ]
print(elementos[3])

#Ejercicio3
lista_vacia = []

lista_vacia.append("leon")
lista_vacia.append("tigre")
lista_vacia.append("oso")

print(lista_vacia)

#Ejercicio4
animales = ["perro", "gato", "conejo", "pez"]

animales [1] = "loro"
animales [3] = "oso"
print(animales)

#Ejercicio5
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#"Se hace una lista de números y numeros.remove(max(numeros)) borra el número más grande de la lista."

#Ejercicio6
numero = list(range(10,31,5))

print(numero[0:2])

#Ejercicio7
autos = ["sedan", "polo", "suran", "gol"]

autos [1] = "corolla"
autos [2] = "palio"

print(autos)

#Ejercicio8
dobles = []


dobles.append(10)
dobles.append(20)
dobles.append(30)
print (dobles)

#Ejercicio9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
                  
print(compras)

#Ejercicio10
lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

print(lista_anidada)
