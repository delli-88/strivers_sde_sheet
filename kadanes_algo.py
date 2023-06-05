from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    
    if n==1:
        return arr[0]

    global_max = 0
    max_till_now = 0
    for i in range(n):
        max_till_now = max(max_till_now+arr[i],arr[i])
        global_max = max(max_till_now,global_max)
    return global_max
































#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
