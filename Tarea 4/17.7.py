class Nodo:
    def __init__(self, valor=None, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def fusionar_listas(lista1, lista2):
    cabeza = Nodo()  # Nodo ficticio para la cabeza
    actual = cabeza

    while lista1 is not None and lista2 is not None:
        if lista1.valor < lista2.valor:
            actual.siguiente = lista1
            lista1 = lista1.siguiente
        else:
            actual.siguiente = lista2
            lista2 = lista2.siguiente

        actual = actual.siguiente

    # Agregar los elementos restantes de ambas listas, si los hay
    if lista1 is not None:
        actual.siguiente = lista1
    elif lista2 is not None:
        actual.siguiente = lista2

    return cabeza.siguiente

def crear_lista_desde_input():
    valores = input("Ingrese los valores separados por espacios: ")
    valores = [int(valor) for valor in valores.split()]
    nodo = None

    for valor in reversed(valores):
        nodo = Nodo(valor, nodo)

    return nodo

def imprimir_lista_enlazada(nodo):
    while nodo is not None:
        print(nodo.valor, end=" ")
        nodo = nodo.siguiente
    print()

# Ingresar las listas desde el usuario
print("Ingrese la primera lista:")
lista1 = crear_lista_desde_input()

print("Ingrese la segunda lista:")
lista2 = crear_lista_desde_input()

# Fusionar las listas y mostrar el resultado
lista_fusionada = fusionar_listas(lista1, lista2)

print("\nLista fusionada:")
imprimir_lista_enlazada(lista_fusionada)
