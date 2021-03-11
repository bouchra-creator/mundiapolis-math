# !/usr/bin/env python3

np_elementwise = __import__('12-bracin_the_elements').np_elementwise
import numpy as np
def np_elementwise(mat1, mat2):
    return np.add(mat1,mat2),np.subtract(mat1,mat2),np.multiply(mat1,mat2),np.divide(mat1,mat2)
mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)