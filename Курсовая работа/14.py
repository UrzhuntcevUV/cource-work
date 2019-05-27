import numpy as np

N = 4
M = 5


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

max_el = np.max(matrix)
matrix = matrix / max_el
print("Полученная матрица:\r\n {}".format(matrix))
