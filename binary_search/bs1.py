"""
출처: 나동빈 이코테2021
내용: 재귀함수 및 찾고자하는 값 + 시작 + 끝점 활용하여 이진탐색 실시
메모: 
"""

n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

result = binary_search(array, target, 0, n-1)
if result is None:
    print("no such value")
else:
    print(f'{result + 1}')

"""
10 7
1 3 5 7 9 11 13 15 17 19
"""