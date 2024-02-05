def suma_recursiva(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + suma_recursiva(arr[1:])


arreglo = [1, 20, 16, 46, 5]
resultado = suma_recursiva(arreglo)
print("La suma recursiva del arreglo es:", resultado)

