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