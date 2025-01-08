import numpy as np

print("LECTURE: -------------------------------")

# multiply a vector or matrix by a scalar
A = np.array([[1,2],[3,4]])
B = 4 * A

print("B: ", B, "\n")

# add equally sized vectors or matrices
A = np.array([[1,2],[3,4]])
B = np.array([[-4,-3],[-2,-1]])
C = A + B

print("C: ", C, "\n")

# Vector dot products can be computed using the np.dot() function:
v = np.array([-1,-2,-3])
u = np.array([2,2,2])
T = np.dot(v,u)

print("T: ", T, "\n")

# Matrix multiplication is computed using either the np.matmul() function or using the @ symbol as shorthand.
# It is important to note that using the typical Python multiplication symbol * will result in an elementwise multiplication instead.

A = np.array([[1,2],[3,4]])
B = np.array([[-4,-3],[-2,-1]])

# one way to matrix multiply
D = np.matmul(A,B)

print("D: ", D, "\n")

# another way to matrix multiply
E = A@B

print("E: ", E, "\n")

print("EXERCISES: -------------------------------")

# Given a 2 x 3 matrix
A = np.array([[2,3,-4], [-2, 1, -3]])

# a 2 x 3 matrix
B = np.array([[1,-1,4], [3,-3,3]])

# a 3 x 2 matrix
C = np.array([[1, 2], [3, 4], [5, 6]])

# Calculate D = 4A - 2B
D = 4*A -2*B
print("D: ", D, "\n")

# Calculate E = AC
E = np.matmul(A,C)
print("E: ", E, "\n")

# Calculate F = CA
F = np.matmul(A,C)
print("F: ", F, "\n")