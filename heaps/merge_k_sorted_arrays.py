from os import *
from sys import *
from collections import *
from math import *
import heapq

def mergeKSortedArrays(kArrays, k:int):
    heap = []

    for i in range(k):
        heap.append((kArrays[i][0],i,0))
    heapq.heapify(heap)

    sol = []
    while heap:
        smallest,row,col = heapq.heappop(heap)
        sol.append(smallest)

        if col+1<len(kArrays[row]):
            heapq.heappush(heap, ((kArrays[row][col+1],row,col+1)))
    return sol




print(mergeKSortedArrays([[3,5,9],[1,2,3,8]],2))