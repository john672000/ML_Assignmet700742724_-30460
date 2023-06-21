"""
b. Write a program to compute the eigenvalues and right eigenvectors of a given square array given below:
[[ 3 -2]
[ 1 0]]
"""

import numpy as np

# Given square array
square_array = np.array([[3, -2],
                         [1, 0]])

# Compute eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(square_array)

"""
Print the eigenvalues 
We can manually calculate eigen values as the following "(3-x)(0-x) - (-2x1)" where x gives the values
"""
print("Eigenvalues:", eigenvalues)

# Print the right eigenvectors
print("Right eigenvectors:")
print(eigenvectors)