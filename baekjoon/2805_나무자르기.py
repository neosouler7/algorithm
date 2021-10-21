"""
comment)
일반 탐색으로 시간초과 발생하니... 이진 탐색!

"""

# 이진 탐색
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().rstrip().split()))
tree.sort()
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for t in tree:
        if t > mid:
            temp += t - mid
    if temp >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# 일반 탐색
# import sys
# N, M = map(int, sys.stdin.readline().rstrip().split())
# tree = list(map(int, sys.stdin.readline().rstrip().split()))
# tree.sort(reverse=True)
# saw = tree[0]
# answer = 0
# while True:
#     temp = 0
#     for t in tree:
#         if t > saw:
#             temp += t - saw
#         else:
#             break
#     if temp >= M:
#         break
#     saw -= 1
# print(saw)