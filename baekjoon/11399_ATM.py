"""
5
3 1 4 3 2

greedy
"""


N = int(input())
array = list(map(int, input().split()))
array.sort()

answer = 0
for i in range(N):
    for j in range(i+1):
        answer += array[j]
print(answer)