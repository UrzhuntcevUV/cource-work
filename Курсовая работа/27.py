import numpy as np

N = 4
M = 5

H = 2


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix_bool = matrix == H
col_sum = np.sum(matrix_bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())

print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())
