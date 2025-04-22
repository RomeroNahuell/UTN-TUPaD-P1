#Ejercicio1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir frutas nuevas con precios
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

#Ejercicio2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir frutas nuevas con precios
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
# Actualizar precios de frutas existentes
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

#Ejercicio3
precios_frutas = {'Banana': 1330 , 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450,'Naranja' : 1200 ,'Manzana' : 1700, 'Pera' : 2300 }

frutas = list(precios_frutas.keys())
print(frutas)

#Ejercicio4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def Saludar(self):
        print(f"Hola soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años. ")

presentacion = Persona("Nahuel","Argentina",24)
presentacion.Saludar()

#Ejercicio5
import math

class Circulo:
    def __init__ (self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * math.pow (self.radio , 2)
        
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
      

calculo = Circulo (4)
area = calculo.calcular_area()
perimetro = calculo.calcular_perimetro()

print(f"el area del circulo es {area}")
print (f"el perimetro del circulo es {perimetro}")

#Ejercicio6
# defino mi estructura y creo la pila y los caracteres a usar en la pila
def balanceado(caract):
    pila = []
    caracteres = {")" : "(", "]" : "[", "}" : "{"}

    for simbolo in caract:
        if simbolo in "([{":
             pila.append(simbolo)

        elif simbolo in ")]}":
            if not pila:
                return False
            ultimo = pila.pop()
            if caracteres [simbolo] != ultimo:
                return False
    return len(pila) == 0

print(balanceado("({[]})"))   
print(balanceado("({[})"))    

#Ejercicio7
from collections import deque

class Cola:
    def __init__(self):
        self.clientes = deque()
    
    def encolar(self, cliente):
        self.clientes.append(cliente)
    
    def desencolar(self):
        return self.clientes.popleft() if not self.esta_vacia() else "La cola está vacía"
    
    def esta_vacia(self):
        return len(self.clientes) == 0
    
    def ver_frente(self):
        return self.clientes[0] if not self.esta_vacia() else "La cola está vacía"

banco = Cola()

banco.encolar("Cliente 1")
banco.encolar("Cliente 2")
banco.encolar("Cliente 3")

print("Siguiente cliente:", banco.ver_frente())  # Cliente 1
print("Atendiendo a:", banco.desencolar())       # Cliente 1
print("Siguiente cliente:", banco.ver_frente())  # Cliente 2
print("Atendiendo a:", banco.desencolar()) 

#Ejercicio8

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__ (self):
        self.cabeza = None
        
    def insertar (self,dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar (self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(4)
lista.insertar(3)
lista.mostrar()

#Ejercicio9
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__ (self):
        self.cabeza = None
        
    def insertar (self,dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar (self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print("None")

    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo


lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(4)
lista.insertar(3)
lista.invertir()
lista.mostrar()