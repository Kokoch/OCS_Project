// Header file for input output functions
#include <stdio.h>

void input(int a[][10], int m, int n) {
    int i, j;
    printf("\nEnter elements of matrix:\n");

    for (i = 0; i < m; ++i) {
        for (j = 0; j < n; ++j) {
            printf("Enter elements a%d%d: ", i + 1, j + 1);
            scanf("%d", & a[i][j]);
        }
    }
}

void display(int a[][10], int m, int n) {
    int i, j;
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            printf("%d", a[i][j]);
        }
    }
}

void multiply(int a[][10], int b[][10], int c[][10], int m, int n, int p, int q) {
    int i, j, k;
    for (i = 0; i < m; ++i) {
        for (j = 0; j < q; ++j) {
            c[i][j] = 0;
        }
    }

    for (i = 0; i < m; ++i) {
        for (j = 0; j < q; ++j) {
            for (k = 0; k < n; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}





int main()
{
    input()
    multiply(A, B, C, 3, 3, 3, 3);

    display(C, 3, 3);
  
    return 0;
}
 
