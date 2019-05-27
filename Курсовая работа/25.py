import numpy as np

N = 4
M = 5

L = 2
K = 2


A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(A))

matrix_bool = A == 0
col = np.sum(matrix_bool, axis=1)
A = np.insert(A, M, col, axis=1)

row = np.append(np.sum(matrix_bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)

print("Полученная матрица:\r\n {}".format(A))
