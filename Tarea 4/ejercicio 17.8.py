import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabecera = None

    def insertar_ordenado(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera == None:
            self.cabecera = nuevo_nodo
            return
        if valor <= self.cabecera.valor:
            nuevo_nodo.siguiente = self.cabecera
            self.cabecera = nuevo_nodo
            return
        actual = self.cabecera
        while actual.siguiente and actual.siguiente.valor < valor:
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabecera
        while actual:
            print(actual.valor, end=' ; ')
            actual = actual.siguiente
        print("terminado")

    def sumar_elementos(self):
        suma = 0
        actual = self.cabecera
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

    def promedio_elementos(self):
        cantidad = 0
        suma = 0
        actual = self.cabecera
        while actual:
            suma += actual.valor
            cantidad += 1
            actual = actual.siguiente
        if cantidad == 0:
            return 0
        return suma / cantidad

#  GENERAMOS LOS 25 ENTEROS ALEATORIOS 
lista = ListaEnlazada()
for _ in range(25):
    lista.insertar_ordenado(random.randint(0, 100))

# LISTA SE IMPRIMA
print("Lista enlazada:")
lista.imprimir()

# SUMA 
suma = lista.sumar_elementos()
print("\nSuma de los elementos:", suma)

# PROMEDIO
promedio = lista.promedio_elementos()
print("Promedio de los elementos:", promedio)
