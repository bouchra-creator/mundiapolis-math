#!/usr/bin/env python3

add_matrices2D = __import__('5-across_the_planes').add_matrices2D
import numpy as np
def add_matrices2D(mat1, mat2):
    mat1 = np.matrix(mat1)
    mat2 = np.matrix(mat2)
    if(np.shape(mat1) == np.shape(mat2) ):
        somme=mat1+mat2
        return somme.tolist()
    else:  
        return "None"

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))