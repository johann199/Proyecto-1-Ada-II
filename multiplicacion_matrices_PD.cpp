#include <iostream>
#include <vector>
using namespace std;
// Programaciòn dinamica para multiplicar dos matrices A y B, y almacenar el resultado en C

// Funciòn para multiplicar dos matrices A y B, y almacenar el resultado en C
void multiplicacion_matrices(int A[4][4], int B[4][4], int C[4][4]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            C[i][j] = 0;
            for (int k = 0; k < 3; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main(){
    // Solicitar los valores de las matrices
    int f1,c1,f2,c2;
    cout << "Ingrese el nùmero de filas y columnas de la matriz A:";
    cin >> f1 >> c1;
    cout << "ingrese el nùmero de filas y columnas de la matriz B:";
    cin >> f2 >> c2; 

    if (c1 != f2) {
        cout << "Error: El nùmero de columnas de la matriz A debe ser igual al de las filas de la matris B"<< endl;
        return 0;
    }

    // Inicio la solución

    double a[f1][c1], b[f2][c2], resultado[f1][c2];

    // datos de entrad matriz A
    cout << "Ingrese los elementos de la matriz A:" << endl;
    for (int i=0; i<f1; i++)
        for (int j=0; j<c1; j++) cin >> a[i][j];

    // datos de entrada matriz B
    cout << "ingrese los elementos de la matriz B;" << endl;
    for (int i=0; i <f2; i++)
        for (int j=0; j<c2; j++) cin >> b[i][j];

    
    // Actualizar la matriz resultante en 0
    for (int i=0; i<f1; i++)
        for(int j=0; j<c2; j++ ) resultado[i][j]=0;
    
    // Multiplicar matrices

    for (int i=0; i<f1; i++){
          for (int j=0; j<c2; j++){
            for(int k=0; k<c1; k++){
                resultado[i][j] += a[i][j] * b[k][j];
            }
        }    
    }
    
    /// Resultado de la multiplicacion de las matrices
    cout << "Matriz resultante " << endl;
    for (int i=0; i<f1; i++){
        for (int j=0; j<c2; j++){
            cout << resultado[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
