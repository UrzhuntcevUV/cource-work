import numpy as np

N = 4
M = 5


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix_bool = matrix < 0
num_cols = np.sum(matrix_bool, axis=0)
num_rows = np.sum(matrix_bool, axis=1)

matrix = np.vstack((matrix, [num_cols]))
matrix = np.column_stack((matrix, np.append(num_rows, 0)))

print("Количество отрицательных элементов в каждом столбце и в каждой строке")
print("Полученная матрица:\r\n {}".format(matrix))
