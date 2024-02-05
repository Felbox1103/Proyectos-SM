a=int(input("Ingrese el primer numero :"))
b=int(input("Ingrese el segundo numero :"))


def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    else:
        return maximo_comun_divisor_recursivo(b, a % b)
print (maximo_comun_divisor_recursivo(a, b))