import numpy as np

N = 4
M = 5

H = 2


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix_bool = matrix == H
row_sum = np.sum(matrix_bool, axis=0)

print("Столбцы в которых встречается значение {}:".format(H))
print(np.argwhere(row_sum).flatten())

print("Столбцы в которых нет значения {}:".format(H))
print(np.argwhere(row_sum == 0).flatten())
