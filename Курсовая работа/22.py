import numpy as np

N = 4
M = 5


A = np.random.randint(low=0, high=2, size=(N, M))
print("Матрица:\r\n{}".format(A))

col = [i % 2 for i in np.sum(A, axis=1)]

A = np.insert(A, M, col, axis=1)
print("Полученная матрица:\r\n {}".format(A))
