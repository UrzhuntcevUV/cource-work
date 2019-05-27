import numpy as np

N = 4
M = 5

K = 2


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

col = matrix[:, K]
col = col.reshape(len(col), 1)

matrix = matrix * col

print("Полученная матрица:\r\n {}".format(matrix))
