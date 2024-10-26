# Ingresar la matriz
def ingresar_matriz():
    matriz = []  # Se corrigió la declaración de la matriz

    print("Introduce los valores de la matriz de 3x3: ")
    for i in range(3):
        fila = []
        for j in range(3):  # Se añadió ':' al final
            valor = float(input(f"Elemento [{i + 1}][{j + 1}]: "))  # Se corrigió el formato de entrada
            fila.append(valor)
        matriz.append(fila)  # Se movió esta línea fuera del bucle interno
    return matriz

# Sumar la matriz
def sumar_matriz(matriz1, matriz2):
    matriz_suma = []  # Se corrigió la declaración de la matriz

    for i in range(3):
        fila = []
        for j in range(3):  # Se añadió ':' al final
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila)  # Se corrigió el nombre de la variable
    return matriz_suma  # Se devolvió la matriz correcta

# Transponer la matriz
def transponer_matriz(matriz):
    matriz_transpuesta = []  # Se corrigió la declaración de la matriz

    for j in range(3):
        fila = []
        for i in range(3):
            fila.append(matriz[i][j])
        matriz_transpuesta.append(fila)  # Se añadió esta línea fuera del bucle interno
    return matriz_transpuesta  # Se devolvió la matriz transpuesta

# Imprimir matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Programa Principal

print("Matriz 1: ")
matriz1 = ingresar_matriz()

print("Matriz 2: ")
matriz2 = ingresar_matriz()

# Suma matriz
matriz_resultante = sumar_matriz(matriz1, matriz2)

# Resultado de la suma
print("El resultado de la suma de las matrices es: ")
imprimir_matriz(matriz_resultante)

# Transponer la matriz
matriz_transpuesta = transponer_matriz(matriz_resultante)

# Resultado de la transposición
print("La matriz transpuesta es: ")
imprimir_matriz(matriz_transpuesta)