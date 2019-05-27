import numpy as np

N = 4
M = 5


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

diagonal_main = np.diagonal(matrix)
print("Элементы главной диагонали:\r\n{}".format(diagonal_main))

sum_diagonal_main = np.sum(diagonal_main)
print("Cумма элементов главной диагонали:\r\n{}".format(sum_diagonal_main))

diagonal_side = np.diagonal(matrix[::-1])
print("Элементы побочной диагонали:\r\n{}".format(diagonal_side))

sum_diagonal_side = np.sum(diagonal_side)
print("сумму элементов побочной диагонали:\r\n{}".format(sum_diagonal_side))
