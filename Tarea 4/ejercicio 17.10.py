def imprimir_en_orden_inverso(texto):
    
    palabras = texto.split()  # divide el texto
    pila = []  # Inicializa una lista que actuará como pila

    # Apila cada palabra en la "pila"
    for palabra in palabras:
        pila.append(palabra)

    # Desapila y muestra cada palabra en orden inverso
    print("Palabras en orden inverso:")
    while pila:
        print(pila.pop(), end=" ")



linea_texto = input("Ingrese un texto texto: ")

# Llamar a la función para imprimir en inverso
imprimir_en_orden_inverso(linea_texto)
