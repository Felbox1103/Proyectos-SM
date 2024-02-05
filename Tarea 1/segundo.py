cantidad_pares = 0
cantidad_impares = 0
suma_pares = 0
suma_impares = 0

for i in range(10):
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:  
        cantidad_pares += 1
        suma_pares += numero
    else:  
        cantidad_impares += 1
        suma_impares += numero

print("Cantidad de números pares:", cantidad_pares)
print("Suma de los números pares:", suma_pares)
print("Cantidad de números impares:", cantidad_impares)
print("Suma de los números impares:", suma_impares)