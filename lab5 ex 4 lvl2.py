import numpy as np
A = np.random.randint(1, 100, (5, 5))
B = np.random.randint(1, 100, (5, 5))
print("Original matrix A:")
print(A)
print("\nOriginal matrix B:")
print(B)
def find_max_index_on_diagonal(matrix):
    max_index = 0
    max_value = matrix[0][0]
    for i in range(1, matrix.shape[0]):
        if matrix[i][i] > max_value:
            max_value = matrix[i][i]
            max_index = i
    return max_index
max_index_A = find_max_index_on_diagonal(A)
max_index_B = find_max_index_on_diagonal(B)
A[max_index_A], B[:, max_index_B] = B[:, max_index_B], A[max_index_A].copy()

print("\nMatrix A after replacement:")
print(A)
print("\nMatrix B after replacement:")
print(B)