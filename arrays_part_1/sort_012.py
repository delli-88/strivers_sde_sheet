from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything
    count_dict = {
         0:0,
         1:0,
         2:0
    }

    for i in range(n):
         count_dict[arr[i]]+=1
    
    ptr = 0
    for _ in range(count_dict[0]):
         arr[ptr] = 0
         ptr+=1
    for _ in range(count_dict[1]):
         arr[ptr] = 1
         ptr+=1
    for _ in range(count_dict[2]):
         arr[ptr] = 2
         ptr+=1
    
    return


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
