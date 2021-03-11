#!/usr/bin/env python3

add_arrays = __import__('4-line_up').add_arrays
import numpy as np

def add_arrays(arr1, arr2):
    if(np.shape(arr1) == np.shape(arr2) ):
        arr= np.add(arr1,arr2)
        return arr.tolist()
    else:  
        return "None"
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./4-main.py 
[6, 8, 10, 12]
[1, 2, 3, 4]
[5, 6, 7, 8]
None