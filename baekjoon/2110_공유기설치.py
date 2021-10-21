"""
5 3
1
2
8
4
9

comment)
어디에 놓을지가 아닌, 얼만큼 떨어진 곳에 두어야 하는가

어렵다... 이해못함

"""
import sys
N, C = map(int, sys.stdin.readline().rstrip().split())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().rstrip()))
array.sort()
start, end = 1, array[-1] - array[0]

answer = 0
while start <= end:
    mid = (start + end) // 2
    prev = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] - prev >= mid:
            count += 1
            prev = array[i]
    
    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)