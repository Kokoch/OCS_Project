import sys
import random

# For command line input. The three parameters must be in the order "size", "range", "type". Size and Range are integer values. Type can only be "int", "neg", "float"
if True:
    m_size = int(sys.argv[1])
    print("Size of the matrix to be generated:", m_size)

    m_range = int(sys.argv[2])
    print("Range of the matrix to be generated:", m_range)

    m_type = str(sys.argv[3])
    print("Type of the values contained in the matrix to be generated:", m_type)
    
else:

    size_list = [2, 3, 5, 8, 10]#[10, 100, 1000, 10000]
    m_size = random.choice(size_list)
    print("Size of the matrix to be generated:", m_size)

    range_list = [10, 100, 1000, 10000]
    m_range = random.choice(range_list)
    print("Range of the matrix to be generated:", m_range)

    type_list = ["int", "neg", "float"]
    m_type = random.choice(type_list)
    print("Type of the values contained in the matrix to be generated:", m_type)
       

def generate_matrix(m_size, m_range, m_type):

    matrix = [ [ 0 for i in range(m_size) ] for j in range(m_size) ]

    for row in range(m_size):
        for column in range(m_size):

            matrix[row][column] = generate_value(m_range, m_type)

    #print(matrix)
    return matrix

def generate_value(m_range, m_type):

    #print(m_range, m_type, type(m_range), type(m_type))

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

    #print("Output MM matrix:", m)
    return m

matrix_A = generate_matrix(m_size, m_range, m_type)
matrix_mul(matrix_A, matrix_A)