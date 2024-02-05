cantidad = int(input("ingresa la cantidad de factores a multiplicar: "))
numeros = []

for i in range(cantidad):
    numero = int(input(f"ingrese el número {i+1}: "))
    numeros.append(numero)
    resultado = 1
for numero in numeros:
    resultado *= numero

print("El resultado de la multiplicación es: ",resultado)
