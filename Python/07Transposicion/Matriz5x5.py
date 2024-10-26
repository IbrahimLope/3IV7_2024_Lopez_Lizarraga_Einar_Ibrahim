# Ingresar la matriz
def ingresar_matriz():
    matriz = []  # Se inicializa la matriz

    print("Introduce los valores de la matriz de 5x5: ")
    for i in range(5):
        fila = []
        for j in range(5):  # Cambiado a 5
            valor = float(input(f"Elemento [{i + 1}][{j + 1}]: "))  # Entrada del valor
            fila.append(valor)
        matriz.append(fila)  # Se añade la fila a la matriz
    return matriz

# Sumar la matriz
def sumar_matriz(matriz1, matriz2):
    matriz_suma = []  # Se inicializa la matriz de suma

    for i in range(5):
        fila = []
        for j in range(5):  # Cambiado a 5
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila)  # Se añade la fila de suma
    return matriz_suma  # Se devuelve la matriz de suma

# Transponer la matriz
def transponer_matriz(matriz):
    matriz_transpuesta = []  # Se inicializa la matriz transpuesta

    for j in range(5):
        fila = []
        for i in range(5):
            fila.append(matriz[i][j])
        matriz_transpuesta.append(fila)  # Se añade la fila transpuesta
    return matriz_transpuesta  # Se devuelve la matriz transpuesta

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

# Transponer la matriz resultante
matriz_transpuesta = transponer_matriz(matriz_resultante)

# Resultado de la transposición
print("La matriz transpuesta es: ")
imprimir_matriz(matriz_transpuesta)

