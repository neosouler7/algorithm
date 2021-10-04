"""
출처: 나동빈 이코테2021
내용: 값이 특정 범위에 속하는 데이터 개수 찾기
메모: 정렬 순서를 유지하며 왼쪽/오른쪽에 삽입될 index를 반환하는 내장함수 활용
"""

from bisect import bisect_left, bisect_right

def count_by_range(array, left, right):
    r_idx = bisect_right(array, right)
    l_idx = bisect_left(array, left)
    return r_idx - l_idx

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))