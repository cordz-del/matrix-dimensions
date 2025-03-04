Creating matrices and checking their shapes
Performing matrix (dot) multiplication
Element-wise multiplication
Transposing matrices
Inverting a square matrix and validating the inversion

import numpy as np

# --- Creating Matrices and Checking Dimensions ---
# Define a 2x3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print("Matrix A:")
print(A)
print("Shape of A:", A.shape)  # Output: (2, 3)

# Define a 3x2 matrix
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])
print("\nMatrix B:")
print(B)
print("Shape of B:", B.shape)  # Output: (3, 2)

# --- Matrix Multiplication (Dot Product) ---
# Multiply A (2x3) by B (3x2) to get a 2x2 matrix
C = np.dot(A, B)
print("\nMatrix C = A dot B:")
print(C)
print("Shape of C:", C.shape)  # Output: (2, 2)

# --- Element-wise Multiplication ---
# For element-wise multiplication, the matrices must have the same dimensions.
# Here, we create another 2x3 matrix D
D = np.array([[1, 2, 3],
              [4, 5, 6]])
E = A * D  # Element-wise multiplication
print("\nElement-wise multiplication of A and D:")
print(E)

# --- Transposing a Matrix ---
A_transposed = A.T
print("\nTranspose of Matrix A:")
print(A_transposed)
print("Shape of A_transposed:", A_transposed.shape)  # Output: (3, 2)

# --- Inverting a Square Matrix ---
# Define a square matrix F (2x2)
F = np.array([[1, 2],
              [3, 4]])
print("\nSquare Matrix F:")
print(F)

# Compute the inverse of F
F_inv = np.linalg.inv(F)
print("\nInverse of Matrix F:")
print(F_inv)

# Verify the inversion: F * F_inv should be the identity matrix
Identity = np.dot(F, F_inv)
print("\nProduct of F and its Inverse (Identity Matrix):")
print(Identity)
