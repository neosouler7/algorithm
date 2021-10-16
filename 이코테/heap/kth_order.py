"""
출처: 작자 미상의 블로그
내용: -
메모: 순서를 고려하여 저장되는 heap 특성 상, 한번 heap을 거쳤다 나오면 정렬이 된다. (default: minHeap)
"""
import heapq

def kth_smallest(array, k):
    heap = []
    for a in array:
        heapq.heappush(heap, a)
    
    answer = heapq.nsmallest(k, heap)[-1]
    return answer

def kth_biggest(array, k):
    heap = []
    for a in array:
        heapq.heappush(heap, a)
    
    answer = heapq.nlargest(k, heap)[-1]
    return answer

array = [4, 1, 7, 3, 8, 5]  # 1 3 4 5 7 8 
k = 3
print(kth_smallest(array, k))
print(kth_biggest(array, k))