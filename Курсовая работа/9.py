import numpy as np

N = 4
M = 5

L = 2
K = 2


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix_slice = matrix[:L, :K]
print("Срез:\r\n{}".format(matrix_slice))

slice_bool = matrix_slice == 0

count_zero_elements = slice_bool.sum()
print("Количество нулевых элементов в срезе: {}".format(count_zero_elements))
