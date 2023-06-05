from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    isRowZero = False
    isColZero = False
    n = len(matrix)
    for i in range(n):
        if matrix[0][i]==0:
            isRowZero==True
            break
    for i in range(n):
        if matrix[i][0]==0:
            isColZero==True
            break
    
    for i in range(1,n):
        for j in range(1,n):
            if matrix[i][j]==0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1,n):
        for j in range(1,n):
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j] = 0

    if isRowZero:
        for i in range(n):
            matrix[0][i]=0
            
    if isColZero:
        for i in range(n):
            matrix[i][0]=0
    
    return matrix
    
print(setZeros([[1,2,3],[4,0,6],[7,8,9]]))