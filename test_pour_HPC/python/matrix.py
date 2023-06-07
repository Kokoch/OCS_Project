import sys
import random

# For command line input. The three parameters must be in the order "size", "range", "type". Size and Range are integer values. Type can only be "int", "neg", "float"
if True:
    m_size = int(sys.argv[1])

    m_range = int(sys.argv[2])

    m_type = str(sys.argv[3])
    
       

def generate_matrix(m_size, m_range, m_type):

    #Add selection of size between 1 and 4:
    if m_size == 1:
        size = 10
    elif m_size == 2:
        size = 100
    elif m_size == 3:
        size = 1000
    elif m_size == 4:
        size = 10000
    else:
        size = m_size
        
    # modified variable m_size to size here.
    matrix = [ [ 0 for i in range(size) ] for j in range(size) ]

    for row in range(size):
        for column in range(size):

            matrix[row][column] = generate_value(m_range, m_type)

    return matrix

def generate_value(m_range, m_type):

    # Positive integers (N)
    if m_type == "int" or m_type == None or m_type == 1 or m_type == "1":
        value = random.randint(0, m_range)

    # Negative integers (Z)
    if m_type == "neg" or m_type == 2 or m_type == "2":
        value = random.randrange(-m_range/2, m_range/2)

    # Floats (R)
    if m_type == "float" or m_type == 3 or m_type == "3":
        value = random.uniform(-m_range/2, m_range/2)
   
    return value

# Given two square matrices
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

matrix_A = generate_matrix(m_size, m_range, m_type)
matrix_mul(matrix_A, matrix_A)