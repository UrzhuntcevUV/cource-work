import numpy as np

N = 4
M = 5


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

sum_elements = np.sum(matrix)
print("Cумма элементов всей матрицы: {}".format(sum))

sum_cols = np.sum(matrix, axis=0)
print("Cумма элементов столбцов:\r\n {}".format(sum_cols))

matrix = np.vstack((matrix, [sum_cols/sum_elements]))
print("Полученная матрица:\r\n {}".format(matrix))
