a=int(input("Ingresa el primer número: "))
b= int(input("Ingresa el segundo número: "))

print("opciones:")
print("1.suma")
print("2.resta")
print("3.multiplicación")
print("4.división")
c=str(input("Ingresa la operacion a realizar: "))

if c == 'suma':
    print("La suma es ", a+b)
if c == 'resta':
    print("La resta es ", a-b)
if c == 'multiplicación':
    print("La mutiplicación es ", a*b)
if c == 'división':
    print("La división es ", a/b)
else:
    print("Opcion Desconocida, recargue el programa")