"""
출처: 작자 미상의 블로그
내용: -
메모: 순서를 고려하여 저장되는 heap 특성 이용.
"""


import heapq

def heap_sort_asc(array):
    heap = []
    for a in array:
        heapq.heappush(heap, a)
    # heapq.heapify(array)  # 기존 리스트를 heap으로 변환
    
    answer = []
    while heap:
        answer.append(heapq.heappop(heap))
    return answer

def heap_sort_desc(array):
    heap = []
    for a in array:
        heapq.heappush(heap, -a)
    # heapq.heapify(array)  # 기존 리스트를 heap으로 변환
    
    answer = []
    while heap:
        answer.append(-heapq.heappop(heap))
    return answer

array = [1, 3, 5, 4, 6, 9, 8, 0]
print(heap_sort_asc(array))
print(heap_sort_desc(array))