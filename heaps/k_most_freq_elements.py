import os
import sys
from collections import *
from math import *
import heapq
from typing import List


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:

    freq_hash = {}

    for i in range(n):
        freq_hash[arr[i]] = freq_hash.get(arr[i],0)+1

    heap = []
    sol = []
    for key,val in freq_hash.items():
        heapq.heappush(heap,(val,key))
        if len(heap)>k:
            heapq.heappop(heap)
    

    keys = [j for _,j in heap]
    keys.sort()

    return keys