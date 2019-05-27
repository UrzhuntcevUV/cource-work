import numpy as np

N = 4
M = 5


A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(A))

row = np.sum(A, axis=0) * -1

A = np.insert(A, N, row, axis=0)
print("Полученная матрица:\r\n {}".format(A))
