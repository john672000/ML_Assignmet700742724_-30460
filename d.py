"""
Write a NumPy program to create a new shape to an array without changing its data.
Reshape 3x2:
[[1 2]
[3 4]
[5 6]]
Reshape 2x3:
[[1 2 3]
[4 5 6]]
"""

import numpy as np
def reshape_3x2(a,r,c):
    l = np.reshape(a, (r, c))
    return l

array = []
print("The Array Contains 1, 2, 3, 4, 5, 6 ")
for x in range (1,7):
    array.append(x)

print(array)
print("Enter the Rows and Coloums you want the array to be reshaped as : ")
print("Rows : ")
r = int(input())
print("Coloums: = ")
c = int(input())
new_array = reshape_3x2(array,r,c)
print(new_array)