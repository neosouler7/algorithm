from itertools import combinations

N, M = map(int, input().split())
array = list()
for _ in range(N):
    array.append(list(map(int, input().split())))

home_total = []
chicken_total = []
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            home_total.append((i, j))
        if array[i][j] == 2:
            chicken_total.append((i, j))

chicken_comb = list(combinations(chicken_total, M))


import sys
answer = list()
for comb in chicken_comb:
    sub_answer_sum = 0
    for home in home_total:
        sub_answer = sys.maxsize
        for target in comb:
            d = abs(home[0] - target[0]) + abs(home[1] - target[1])
            sub_answer = min(sub_answer, d)
        sub_answer_sum += sub_answer
    answer.append(sub_answer_sum)

print(min(answer))




"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

"""