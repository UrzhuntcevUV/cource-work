import numpy as np

N = 4
M = 5

L = 2
K = 2

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(A))

parts = [
    A[:L, :K],
    A[:L, K:],
    A[L:, :K],
    A[L:, K:],
]

for i in range(len(parts)):
    print("Cумма элементов {} части: {}".format(i+1, np.sum(parts[i])))
