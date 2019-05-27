import numpy as np

N = 4
M = 5

K = 1


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

col = np.random.randint(low=-9, high=10, size=N)
print("Столбец для вставки: {}".format(col))

matrix = np.insert(matrix, K, col, axis=1)
print("Полученная матрица:\r\n {}".format(matrix))
