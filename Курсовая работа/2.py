import numpy as np

N = 4
M = 5

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

average = np.average(matrix, axis=1)
print("Cредние значения для каждой строки:\r\n {}".format(average))

max_average = np.max(average)
print("Наибольшее среднее значение: {}".format(max_average))
