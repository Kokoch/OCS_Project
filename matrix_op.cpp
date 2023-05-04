#include <iostream>
using namespace std;

int *matrix_mult(int m1[3][3], int m2[3][3]) {
    int size = sizeof(m1[0]) / sizeof(int);
    printf("%d", size);


    int m[size][size];

    for (int i=0; i < size; i++) {
        for (int j=0; j < size; j++) {
            int result = 0;
            for (int n=0; n < size; n++) {
                result += m1[i][n] * m2[n][j];
            }
            m[i][j] = result;
        }
    }

    return m;
}

int main() {
  int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

  printf("%d", matrix_mult(a, a));

  return 0;
}