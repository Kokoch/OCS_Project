import sys
import ast

matrix_str= sys.argv[1]
matrix = ast.literal_eval(matrix_str)



>>>>>>> b0204bd174e8b933c0ca73b11bcb55880fbdb0e4

#Given two square matrices
def matrix_mul(m1, m2):

    size = len(m1)
    m = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            result = 0
            for n in range(size):
                    result += m1[i][n] * m2[n][j]

            m[i][j] = result

    return m

matrix_mul(A, A)