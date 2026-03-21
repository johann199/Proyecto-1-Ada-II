#include <iostream>
using namespace std;

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
    int A[4][4] = {{1, 2, 3, 4},
                   {5, 6, 7, 8},
                   {9, 10, 11, 12},
                   {13, 14, 15, 16}};


    int B[4][4] = {{9, 8, 7, 6},
                   {5, 4, 3, 2},
                   {1, 0, -1, -2},
                   {-3, -4, -5, -6}};

    int C[4][4];

    multiplicacion_matrices(A, B, C);

    cout << "Resultado de la multiplicación de matrices A y B:" << endl;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4  ; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
