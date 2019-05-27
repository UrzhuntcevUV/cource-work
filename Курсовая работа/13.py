import numpy as np

N = 4
M = 5


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

col_max = np.max(matrix, axis=0)
matrix = matrix / col_max
print("Полученная матрица:\r\n {}".format(matrix))
