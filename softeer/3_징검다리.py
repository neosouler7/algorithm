"""
5
3 2 1 4 5

9
3 2 1 4 5 10 6 7 8
"""

N = int(input())
array = list(map(int, input().split()))

rocks = [1] * N  # n번째 돌을 밟을 수 있는 최대 돌의 개수

for i in range(len(rocks)):
    if i == 0:
        continue
    temp = []
    for j in range(i):
        if array[i] > array[j]:
            temp.append(rocks[j])
    if len(temp) > 0:
        rocks[i] = max(temp) + 1

print(max(rocks))