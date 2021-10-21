"""
comment)


-10 2 3 6 10



"""

import sys
N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()
M = int(sys.stdin.readline().rstrip())
target = list(map(int, sys.stdin.readline().rstrip().split()))

from bisect import bisect_left, bisect_right
answer = []
for t in target:
    if bisect_left(array, t) == bisect_right(array, t):
        answer.append(0)
    else:
        answer.append(1)
print(*answer)