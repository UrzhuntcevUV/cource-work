import numpy as np

N = 4
M = 5


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

row_max = np.max(matrix, axis=1)
matrix = matrix / row_max.reshape(len(row_max), 1)
print("Полученная матрица:\r\n {}".format(matrix))
