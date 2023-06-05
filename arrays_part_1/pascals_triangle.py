from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    triangle = [[1]]
    if n==1:
        return triangle

    for i in range(1,n):
        row = [1]
        for j in range(i-1):
            row.append(triangle[i-1][j]+triangle[i-1][j+1])
        row.append(1)
        triangle.append(row)
    return triangle

print(printPascal(2))