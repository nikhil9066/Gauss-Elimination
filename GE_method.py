import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    A = A.astype(np.float64)
    b = b.astype(np.float64)
    
    # Augment the matrix A with vector b
    augmented_matrix = np.column_stack((A, b))
    print(augmented_matrix)

# Example usage:
A = np.array([[1, 2, -1],
              [2, 1, 1],
              [-1, 0, 1]])

b = np.array([2, 7, 2])

x = gaussian_elimination(A, b)