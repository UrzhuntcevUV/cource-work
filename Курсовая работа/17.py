import numpy as np

N = 4
M = 5

L = 1


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

row = np.random.randint(low=-9, high=10, size=M)
print("Строка для вставки: {}".format(row))

matrix = np.insert(matrix, L, row, axis=0)
print("Полученная матрица:\r\n {}".format(matrix))
