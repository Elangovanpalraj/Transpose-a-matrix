# Transpose a matrix in Single line in Python
# ============================================\n
'''
Input: [[1,2],[3,4],[5,6]]
Output: [[1,3,5],[2,4,6]]
Explanation: Suppose we are given a matrix
                       [[1, 2],
                        [3, 4],
                        [5, 6]]
Then the transpose of the given matrix will be, 
                       [[1, 3, 5],
                        [2, 4, 6]]
'''
# types
# ====\n
# Using List Comprehension
# Using zip
# Using NumPy
# Using itertools
# =============================================================\n
# Python NumPy
# ==========\n
import numpy
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))
