import numpy as np
"""
The Python library NumPy provides a powerful tool to programmatically perform linear algebra.
A fundamental building block of NumPy, the NumPy array allows us to represent vectors and matrices.

These arrays can perform operations directly, such as addition
and scalar multiplication using + and *, respectively.

NumPy also has built-in functions that allow us to perform more advanced operations
like dot products, transposes, and matrix multiplication.

Finally, NumPy has a numpy.linalg sublibrary that provides more advanced functionality.
This includes finding the norm (or magnitude/length) of a vector, 
finding the inverse of a square matrix, and solving a system of linear equations in Ax=b form.

Given the following system of equations:

 2a + 0b - 2c + 3d = 4
-1a + 4b - 1c + 0d = 1
 3a - 1b - 2c + 2d = 2
-2a - 1b + 3c - 0d = -2

Find the unknowns a, b, c, and d. 
"""
A = np.array([[2,0,-2,3],[-1,4,-1,0],[3,-1,-2,2],[-2,-1,3,0]])
b = np.array([4,1,2,-2])
a,b,c,d = np.linalg.solve(A,b)
print((a,b,c,d))


A = np.array([[0, 2],[1, 2]])
print(A)
 # b = np.array([blank 3,4])