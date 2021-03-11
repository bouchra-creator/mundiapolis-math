#!/usr/bin/env python3
import numpy as np 
def matrix_shape(matrix):
        return list (np.shape(matrix))
mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))