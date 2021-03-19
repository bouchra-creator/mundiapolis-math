#!/usr/bin/env python3


def add_matrices2D(mat1, mat2):
    mat1 = np.matrix(mat1)
    mat2 = np.matrix(mat2)
    if(np.shape(mat1) == np.shape(mat2) ):
        somme=mat1+mat2
        return somme.tolist()
    else:  
        return "None"
