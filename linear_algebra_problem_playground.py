import numpy as np

# Define vectors
a = np.array([3, -1, 2])
b = np.array([0, -1, 1])

# Compute dot product
dot_product = np.dot(a, b)

# Compute magnitudes (norms)
magnitude_a = np.linalg.norm(a)
magnitude_b = np.linalg.norm(b)

# Compute the cosine of the angle
cos_theta = dot_product / (magnitude_a * magnitude_b)

# Compute the angle in radians and then convert to degrees
theta_radians = np.arccos(cos_theta)
theta_degrees = np.degrees(theta_radians)

# Round to the nearest whole number
theta_rounded = round(theta_degrees)

# Print the result
print("The angle between the vectors, rounded to the nearest whole number, is:", theta_rounded, "degrees")