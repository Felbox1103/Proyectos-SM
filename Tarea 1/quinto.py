import math 

x= float(input("Ingrese un valor: "))

y= (((x+x**2)/(5*x+3))+x)*(((x+x**2)/(5*x +3))/((x+x**2)/(5*x+3)+2*x))

print(y)