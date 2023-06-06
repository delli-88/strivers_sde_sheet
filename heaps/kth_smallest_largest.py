import heapq
def kthSmallLarge(arr, n, k):
    # Write your code here
    pass
    min_heap = []
    max_heap = []

    for i in range(k):
        min_heap.append(arr[i])
        max_heap.append(-arr[i])
    
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    # print(max_heap)
    for i in range(k,n):
        if arr[i]>=min_heap[0]:
            heapq.heappushpop(min_heap,arr[i])
        if arr[i]<=-(max_heap[0]):
            heapq.heappushpop(max_heap,-arr[i])
    
    return [-max_heap[0],min_heap[0]]


print(kthSmallLarge([5,6,7,2],4,4))