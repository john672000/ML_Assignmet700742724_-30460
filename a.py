"""
a.
Using NumPy create random vector of size 15 having only Integers in the range 1-20.
1. Reshape the array to 3 by 5
2. Print array shape.
3. Replace the max in each row by 0

"""

import numpy as np
v1 = np.random.randint(1, 21, size=15)
print("Random Vector initiation of Size = 5 and Values from 1-20:\n ", v1)

v2 = v1.reshape(3, 5)
print("Reshaping the vector V1 as a 3x5 Matrix form: \n", v2)


print("Replacing the highest values from each row to 0 in vector V2: ")
v2[np.arange(3), np.argmax(v2, axis=1)] = 0
print(v2)


