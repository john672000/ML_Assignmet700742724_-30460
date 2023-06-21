"""
c. Compute the sum of the diagonal element of a given array.
[[0 1 2]
[3 4 5]]

"""
import numpy as np
# Given array
given_array = np.array([[0, 1, 2],
                        [3, 4, 5]])

# Compute the sum of diagonal elements
diagonal_sum = np.trace(given_array)
"""
This above is a rectangular matrix and the diagonal as MP00 and MP11 as it has only 2 rows 
"""
# Print the sum of diagonal elements
print("Sum of diagonal elements:", diagonal_sum)
