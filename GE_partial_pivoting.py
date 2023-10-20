import numpy as np

n = 100
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 5
    if i > 0:
        A[i, i - 1] = 1
    if i < n - 1:
        A[i, i + 1] = 1
print(A)

b = np.zeros(n)
b[49] = 1 
print(b)

def gaussElimination(A, b):
    n = len(b)
    x = np.zeros(n)
    # print("Matrix A:\n", A)
    # print("Vector b:\n", b)

    x[-1] = b[-1] / A[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

x = gaussElimination(A, b)