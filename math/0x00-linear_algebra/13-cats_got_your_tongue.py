#!/usr/bin/env python3
np_cat = __import__('13-cats_got_your_tongue').np_cat
import numpy as np
def np_cat(mat1, mat2, axis=0):
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        return np.concatenate((mat1,mat2),axis=0)
    elif (len(mat1) == len(mat2)) and axis == 1:
        return np.concatenate((mat1,mat2),axis=1)
    else:
        return None
mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])
mat3 = np.array([[7], [8]])
print(np_cat(mat1, mat2))
print(np_cat(mat1, mat2, axis=1))
print(np_cat(mat1, mat3, axis=1))