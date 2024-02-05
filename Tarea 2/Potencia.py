b=int(input("Ingresa la base :"))
p=int(input("Ingresa la potencia :"))

def potencia(p):
    if p==1:
        return b
    else:
        return b*potencia(p-1)
        
print("La potencia es :", potencia(p))