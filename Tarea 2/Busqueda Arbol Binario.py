tamaño_lista = int(input("¿Cuantos numeros desea ingresar? :"))
L = []

for x in range (tamaño_lista):
    numeros = int(input("Ingrese numero para la lista :"))
    L.append(numeros)
print(L)

a=int(input("Ingresa el numero a buscar :"))

def binary_search(a,L,low,high):
    
    if  low <= high:

        mid = (high+low)//2

        if L[mid] < a:
            return binary_search(a,L,mid+1,high)

        elif L[mid] > a:
            return binary_search(a,L,low,mid-1)
        
        else: 
            return mid

    return -1
 
index = binary_search(a,L,0,len(L))

if index == -1:
    print("El numero solicitado no existe.")
else:
    print("El valor solicitado se encuentra en la posición :", index)