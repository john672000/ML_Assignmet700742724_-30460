"""
Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements), also print the shape, type and data type
of the array.
b. Write a program to compute the eigenvalues and right eigenvectors of a given square array given below:
[[ 3 -2]
[ 1 0]]

"""
import numpy as np
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
v1 = np.array(l1, dtype=np.int32)  # (4 bytes = 4x8 = 32bit)
print(v1)
v2 = v1.reshape(4, 3)
print(v2)

# Print the shape of the array
print("Array shape:", v2.shape)

# Print the type of the array
print("Array type:", type(v2))

# Print the data type of the array
print("Array data type:", v2.dtype)
