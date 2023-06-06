import os
import sys
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    duplicate = None
    for i in range(n):
        arr[(arr[i]%n)-1]+=n
    
    for i in range(n):
        if arr[i]//n>1:
            duplicate = i+1
            break
    return duplicate


print(findDuplicate([3,1,3,4,2],5))