class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.encabezado = None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.encabezado:
            self.encabezado = nuevo_nodo
        else:
            actual = self.encabezado
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_cadena(self):
        cadena = ""
        actual = self.encabezado
        while actual:
            cadena += str(actual.dato) + " "
            actual = actual.siguiente
        return cadena.strip()

class ConcatenarLista:
    
    def concatenar(lista1, lista2):
        if not lista1.encabezado:
            lista1.encabezado = lista2.encabezado
        else:
            actual = lista1.encabezado
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = lista2.encabezado

def obtener_lista():
    lista = ListaEnlazada()
    elementos = input("Ingrese los elementos de la lista separados por espacios: ").split()
    for elemento in elementos:
        lista.insertar_al_final(elemento)
    return lista

# Obtener listas enlazadas del usuario
print("Ingrese los elementos de la primera lista:")
lista1 = obtener_lista()
print("Ingrese los elementos de la segunda lista:")
lista2 = obtener_lista()

# Concatenar listas
ConcatenarLista.concatenar(lista1, lista2)

# Obtener cadena resultante
cadena_concatenada = lista1.obtener_cadena()

print("Cadena concatenada:", cadena_concatenada)
