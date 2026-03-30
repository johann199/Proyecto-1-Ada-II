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

def voraz_matrices(p):
    p = p.copy()    # Evitar modificar la lista original
    costo_total = 0
    orden = []
    # Encontrar la multiplicación más barata (mínimo p[i-1] * p[i] * p[i+1])
    while len(p) > 2:
        min_costo = math.inf
        min_idx = -1
        for i in range(1, len(p) - 1):
            costo = p[i-1] * p[i] * p[i+1]
            if costo < min_costo:
                min_costo = costo
                min_idx = i

        costo_total += min_costo
        orden.append(min_idx)

        p.pop(min_idx)

    return costo_total, orden

if __name__ == "__main__":
    num_matrices = int(input("¿Cuántas matrices deseas multiplicar? "))
    p = []
    for i in range(1, num_matrices + 1):
        filas = int(input(f"Filas de M{i}: "))
        columnas = int(input(f"Columnas de M{i}: "))
        if i == 1:
            p.append(filas)
        p.append(columnas)

    costo, orden = voraz_matrices(p)
    print(f"Costo mínimo voraz: {costo}")
    print(f"Orden de multiplicación (índices de fusión): {orden}")

