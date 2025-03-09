import numpy as np

# Define your matrices
A = np.array([
    [2,-3,1],
    [-2,-1,4],
    [0,2,2]
])

B = np.array([
    [3,-2,1],
    [1,-1,2],
    [-2,2,0]
])

# Compute the product
C = np.dot(A, B)

print(C)