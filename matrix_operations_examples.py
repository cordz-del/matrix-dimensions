import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
print("Matrix Multiplication:\n", C)

# Matrix transposition
A_transpose = A.T
print("Transpose of A:\n", A_transpose)

# Matrix inversion
A_inverse = np.linalg.inv(A)
print("Inverse of A:\n", A_inverse)

# Identity matrix
I = np.eye(2)
print("Identity Matrix:\n", I)

# Determinant of a matrix
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# Eigenvalues and eigenvectors of a matrix
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)
