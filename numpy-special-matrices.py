import numpy as np

print("LECTURE: -------------------------------")

# An identity matrix can be constructed using the np.eye() functions, which takes an integer
# argument that determines the n x n size of the square identity matrix.

# 4x4 identity matrix
identity = np.eye(4)
print("\nidentity: \n", identity)

# A matrix or vector of all zeros can be constructed using the np.zeros() function, which takes in a tuple
# argument for the shape of the NumPy array filled with zeros.

# 5-element vector of zeros
zero_vector = np.zeros(5)
print("\nzero_vector: \n", zero_vector)

# 3x2 matrix of zeros
zero_matrix = np.zeros((3,2))
print("\nzero_matrix: \n", zero_matrix)

# The transpose of a matrix can be accessed using the .T attribute of a NumPy array as shown below:
A = np.array([[1,2],[3,4]])
A_transpose = A.T

# If we print A and A_transpose out in the terminal, A outputs as:
# [[1 2]
# [3 4]]

print("\nA: \n", A)

# While A_transpose outputs as:
# [[1 3]
# [2 4]]
print("\nA_transpose: \n", A_transpose)

print("EXERCISES: -------------------------------")

# Given
A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])