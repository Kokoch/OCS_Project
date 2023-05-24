import sys

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_size = int(sys.argv[1])
#print("Matrix received in MM:", m_size)

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