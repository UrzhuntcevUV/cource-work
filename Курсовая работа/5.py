import numpy as np

N = 4
M = 5


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

average_rows = np.average(matrix, axis=1)
print("Cредние значения для каждой строки:\r\n {}".format(average_rows))

average_cols = np.average(matrix, axis=0)
print("Cредние значения для каждого столбца:\r\n {}".format(average_cols))


matrix = np.vstack((matrix, [average_cols]))
matrix = np.column_stack((matrix, np.append(average_rows, 0)))

print("Полученная матрица:\r\n {}".format(matrix))
