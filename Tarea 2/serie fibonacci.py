
          
def fibonacci(n):
       if n <= 1:
        return n
    
       else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numeroTerminos = 5

print("Secuencia de Fibonacci:")
for i in range(numeroTerminos):
    print(fibonacci(i), end=" ")
