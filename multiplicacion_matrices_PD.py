import math

def multiplicacion_matrices(A, B):
    # Obtener las dimensiones de las matrices
    m = int(input("Ingrese el número de filas de A: "))
    n = int(input("Ingrese el número de columnas de A: "))
    p = int(input("Ingrese el número de columnas de B: "))
    q = int(input("Ingrese el número de filas de B: "))

    # Inicializar la matriz resultado C con ceros
    C = [[0 for _ in range(p)] for _ in range(m)]

    # Multiplicar las matrices A y B, y almacenar el resultado en C
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Funcion principal para probar la multiplicacion de matrices
if __name__ == "__main__":
    # Definir dos matrices A y B
    A = eval(input("Ingrese los elementos de la matriz A: "))
    B = eval(input("Ingrese los elementos de la matriz B: "))

    # Multiplicar las matrices A y B
    C = multiplicacion_matrices(A, B)

    # Imprimir el resultado
    print("Resultado de la multiplicación de matrices A y B:")
    for fila in C:
        print(fila)

    