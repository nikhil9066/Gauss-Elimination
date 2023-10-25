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
    #print("Matrix A:\n", A)
    #print("Vector b:\n", b)

    for i in range(1, n):
        factor = A[i, i - 1] / A[i - 1, i - 1]
        A[i] -= factor * A[i - 1]
        # print("Vector b after elimination in row {i}:\n{a}")
        # print(b[i])
        b[i] -= factor * b[i - 1]
        # print("Vector b after elimination in row {i}:\n{b}")
        # print(b[i])

    x[-1] = b[-1] / A[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return xA[i, i]

x = gaussElimination(A, b)
# print(f"Solution vector x:\n{x}")

j_values = np.arange(1, n + 1)
# print((x))
plt.plot(j_values, x)
plt.xlabel('j')
plt.ylabel('x[j]')
plt.title('Solution Vector x[j] as a Function of j')
plt.grid(True)
plt.show()