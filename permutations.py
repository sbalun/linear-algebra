import numpy as np

# Define the matrices
A = np.array([
    [1, 4, 7, -2],
    [3, 0, -2, -1],
    [-4, 2, 1, 0],
    [-8, -3, -1, 2]
])

B = np.array([
    [-4, 2, 1, 0],
    [3, 0, -2, -1],
    [-8, -3, -1, 2],
    [1, 4, 7, -2]
])

# Find the permutation indices
perm = []
for i in range(B.shape[0]):
    match = np.where(np.all(A == B[i], axis=1))[0]
    if len(match) > 0:
        perm.append(match[0])
perm = np.array(perm)
print("Permutation indices:", perm)

# Create the permutation matrix
P_R = np.eye(A.shape[0], dtype=int)
P_R = P_R[perm]
print("Permutation matrix P_R:\n", P_R)

# Verify the solution
result = np.dot(P_R, A)
print("Result of P_R * A:\n", result)

if np.array_equal(result, B):
    print("The permutation matrix is correct!")
else:
    print("There’s an issue with the permutation.")