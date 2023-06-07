import os
import sys
from collections import *
from math import *

def heapify(arr, n, i):
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

# iterative heapify
# def heapify(arr, n, i):
#     smallest = i
#     while True:
#         left_child = 2 * i + 1
#         right_child = 2 * i + 2

#         if left_child < n and   arr[left_child]<arr[smallest]:
#             smallest = left_child

#         if right_child < n and  arr[right_child]< arr[smallest]:
#             smallest = right_child

#         if smallest == i:
#             break

#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         i = smallest



def minHeap(N: int, Q):
    min_heap = []
    sol = []

    for i in range(len(Q)):
        # insert
        if Q[i][0] == 0:
    
            min_heap.append(Q[i][1])
            for i in range((len(min_heap)//2)-1,-1,-1):
                heapify(min_heap, len(min_heap), i)
                
        # delete
        else:
            if min_heap:
                smallest = min_heap[0]
                sol.append(smallest)
                min_heap[0],min_heap[len(min_heap)-1] = min_heap[len(min_heap)-1],min_heap[0] 
                min_heap.pop()
                # for i in range((len(min_heap)//2)-1,-1,-1):
                heapify(min_heap, len(min_heap), 0)

    return sol
