"""
comment)
탐색 문제. 이진으로 해보자
"""
import sys
K, N = map(int, sys.stdin.readline().rstrip().split())
array = []
for _ in range(K):
    array.append(int(sys.stdin.readline().rstrip()))
start, end = 1, max(array)

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for a in array:
        temp += a // mid
    if temp >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)