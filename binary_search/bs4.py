"""
출처: 나동빈 이코테2021
내용: 정렬된 배열에서 특정 개수 구하기
메모: 탐색(bisect) / 개수(counter) 관련 python 내장함수!!

"""

n, x = map(int, input().split())
array = sorted(list(map(int, input().split())))

# from collections import Counter
# def solution(array, x):
#     return dict(Counter(array)).get(x, -1)


from bisect import bisect_left, bisect_right
def solution(array, x):
    r_idx = bisect_right(array, x)
    l_idx = bisect_left(array, x)
    return r_idx - l_idx if r_idx > l_idx else -1

print(solution(array, x))

"""
7 2
1 1 2 2 2 2 3
"""