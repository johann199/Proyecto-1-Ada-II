import math

def multiplicacion_matrices(A, B):
    # Obtener las dimensiones de las matrices
    m= len(A)
    n = len(A[0])
    p = len(B[0])

    if len(B) != n:
        raise ValueError("Columnas de A deben ser iguales a filas de B")

    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

#Aplicamos la programacion dinamica para calcular el costo de multiplicacion de matrices
def costo_multiplicacion(p, i, j, memo, s):

    if i == j: # Caso base: una sola matriz 
        return 0
    
    if memo[i][j] != -1: # ya esta calculado el costo para esta subcadena
        return memo[i][j] # devolver el costo almacenado en memo
    min_cost = math.inf
    for k in range(i, j):
        cost = costo_multiplicacion(p, i, k, memo, s) + costo_multiplicacion(p, k + 1, j, memo, s) + p[i - 1] * p[k] * p[j]
        if cost < min_cost:
            min_cost = cost
            s[i][j] = k # Guardar el punto de división óptimo
    memo[i][j] = min_cost
    return min_cost

# Función para imprimir la secuencia óptima de multiplicación
def imprimir_optimo(s, i, j):
    if i == j:
        print(f"M{i}", end="")
    else:
        print("(", end="")
        imprimir_optimo(s, i, s[i][j])
        imprimir_optimo(s, s[i][j] + 1, j)
        print(")", end="")




# Funcion principal para probar la multiplicacion de matrices
if __name__ == "__main__":
    # Definir dos matrices A y B
    num_matrices = int(input("¿Cuántas matrices deseas multiplicar?"))

    p = []

    for i in range (1, num_matrices + 1):
        filas = int(input(f"¿Cuántas filas tiene la matriz M-{i}?"))
        columnas = int(input(f"¿Cuántas columnas tiene la matriz M-{i}?"))
        if i == 1:
            p.append(filas)
        p.append(columnas)
    
    # inicicializar la matriz de memoizacion
    n = len(p) - 1
    memo = [[-1] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    costo = costo_multiplicacion(p, 1, n, memo, s)
    print(f"El costo mínimo de multiplicar las matrices es: {costo}")

    print("La secuencia óptima de multiplicación es: ", end="")
    imprimir_optimo(s, 1, n)
    print()

    # Tabla de costos 
    print("\nTabla de costos:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if memo[i][j] == -1:
                print(f"{'0':>8}", end="")
            else:
                print(f"{memo[i][j]:>8}", end="")
        print()
    
    # Tabla de decisiones
    print("\nTabla de decisiones (puntos de división óptimos):")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{s[i][j]:>8}", end="")
        print()


