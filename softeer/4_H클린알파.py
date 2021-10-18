"""
3 3
1 2 3
"""
import sys
P, N = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
answer = [0] * N
for i in range(N):
    if i == 0:
        answer[i] = array[i]
        continue
    answer[i] = (answer[i-1]*P + array[i]) % 1000000007
print(answer[-1])