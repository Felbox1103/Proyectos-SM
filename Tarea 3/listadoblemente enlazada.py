class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamañodelista = 0
        
    def vacia(self):
        return self.primero == None

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            encabezado = self.ultimo
            self.ultimo = encabezado.siguiente = Nodo(dato)
            self.ultimo.anterior = encabezado
        self.tamañodelista += 1

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            encabezado = Nodo(dato)
            encabezado.siguiente =  self.primero
            self.primero.anterior = None
            self.primero = encabezado
        self.tamañodelista += 1
            

    def recorrer_inicio(self):
        encabezado = self.primero
        while encabezado != None:
            print(encabezado.dato)
            encabezado = encabezado.siguiente

    def recorrer_final(self):
        encabezado = self.ultimo
        while encabezado:
            print(encabezado.dato)
            encabezado = encabezado.anterior
    

    def eliminar_inicio(self):
            if self.vacia():
               print("Lista vacía")
            elif self.primero.siguiente == None:
                 self.primero = self.ultimo = None
                 self.tamañodelista = 0
            else:
                 self.primero = self.primero.siguiente
                 self.primero.anterior = None
                 self.tamañodelista -= 1

    def eliminar_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.tamañodelista = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.tamañodelista -= 1

try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDoblementeEnlazada()
        while opcion != 8:
            print("******** Lista Doblemente Enlazada **********\n 1. Agregar al final\n 2. Eliminar al final\n 3. ¿Está vacía la lista?\n 4. Agregar al inicio\n 5. Eliminar al inicio\n 6. Mostrar en orden ascendente\n 7. Mostrar en orden descendente\n 8. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregar_final(dato)
            elif opcion == 2:
                lista.eliminar_final()
            elif opcion == 3:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 4:
                dato = input("Ingresa un número ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                lista.recorrer_inicio()
            elif opcion == 7:
                lista.recorrer_final()
            elif opcion == 8:
                print("sección finalizada")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)
