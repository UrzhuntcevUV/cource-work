import numpy as np

N = 4
M = 5

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

sum_cols = np.sum(np.absolute(matrix), axis=0)
print("Суммы столбцов:\r\n {}".format(sum_cols))

max_sum = np.max(sum_cols)
max_sum_col = np.argmax(sum_cols)
col = matrix[:, max_sum_col]
print("Наибольшая сумма: {} в столбце №{}".format(max_sum, max_sum_col+1))
print("Элементы столбца: {}".format(col))

max_el = np.max(col)
print("Наибольший элемент: {}".format(max_el))
