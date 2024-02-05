
n = int(input("ingrese el numero: "))
if n >= 0:
    x = 1
    f = 1
    while x <= n:
        f = f*x
        x += 1
    print("El factorial de ",n," es: ",f)
else:
    print(" no se puede calcular el factorial")
          
        
