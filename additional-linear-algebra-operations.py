import numpy as np
#  We will be using the numpy.linalg sublibrary to perform the following operations:
#
# The “norm” (or length/magnitude) of a vector can be found using np.linalg.norm():

v = np.array([2,-4,1])
print("\nGiven array([2,-4,1]):")
v_norm = np.linalg.norm(v)
print("\nv_norm or length/magnitude of vector: \n", v_norm)

# The inverse of a square matrix, if one exists, can be found using np.linalg.inv():

A = np.array([[1,2],[3,4]])
print("\nThe inverse square matrix of A: \n", np.linalg.inv(A))

'''
Finally, we can actually solve for unknown variables in a system on linear equations in Ax=b form
using np.linalg.solve(), which takes in the A and b parameters. Given:

x + 4y -  z = -1
-x - 3y + 2z = 2
2x -  y - 2z = -2
   
We convert to Ax=b form and solve.
'''
# each array in A is an equation from the above system of equations
A = np.array([[1,4,-1],[-1,-3,2],[2,-1,-2]])
# the solution to each equation
b = np.array([-1,2,-2])
# solve for x, y, and z
x,y,z = np.linalg.solve(A,b)

print("\nThe solution is: \n",(x, y, z))

# Given
'''
4x + z = 2
-y + 2z - 3x = 0
.5y - x - 1.5z = -4

Need to list in same order x, y, z.  So rearranged it is
 4x + 0y + 1z  = 2
-3x - 1y + 2z  = 0
-1x +.5y - 1.5z = -4
'''
A = np.array([[4,0,1],[-3,-1,2],[-1,.5,-1.5]])

'''
We now need the b part of our Ax=b form.
'''
b = np.array([2,0,-4])

x,y,z = np.linalg.solve(A,b)

print("\nThe next solution is: \n",(x, y, z))

# Define the vector as a NumPy array
v = np.array([-2, -3, 0, 5, 1])

# Compute the length (magnitude) using numpy's norm function
length_v = np.linalg.norm(v)

# Print the result
print("Length of the vector:", length_v)

