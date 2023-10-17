import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    A = A.astype(np.float64)
    b = b.astype(np.float64)
    
    # Augment the matrix A with vector b
    augmented_matrix = np.column_stack((A, b))
    print(augmented_matrix)

    # Forward elimination
    for i in range(n):
        max_row = i
        for k in range(i+1, n):
            if abs(augmented_matrix[k, i]) > abs(augmented_matrix[max_row, i]):
                max_row = k
        
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        
        augmented_matrix[i] /= augmented_matrix[i, i]
        
        # Eliminate all other entries in the current column
        for j in range(i+1, n):
            augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]
    
    # Back-substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = augmented_matrix[i, -1]
        for j in range(i+1, n):
            x[i] -= augmented_matrix[i, j] * x[j]
    
    return x

A = np.array([[1, 2, -1],
              [2, 1, 1],
              [-1, 0, 1]])

b = np.array([2, 7, 2])

x = gaussian_elimination(A, b)
print("Solution:", x)

# Inbuilt function just in case if ur lazy
# x = np.linalg.solve(A, b)

print("Solution for x:")
print(x)