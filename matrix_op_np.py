import numpy as np

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def matrix__mul_np(m1, m2):
    return np.matmul(m1, m2)

print(matrix__mul_np(A, A))