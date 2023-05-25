import matrix_gen
import random

matrices = []

for s in range(1, 3):
    for t in range(1, 4):
        r  = random.randint(1, 1000)
        m = matrix_gen.generate_matrix(s, r, t)
        m_str = f"{m}".replace(" ", "")
        matrices.append(m_str)


with open('matrix_input.txt', 'w') as f:
    for mtx in matrices:
        f.write(mtx)
        f.write('\n')

