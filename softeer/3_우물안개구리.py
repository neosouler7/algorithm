"""
5 3
1 2 3 4 5
1 3
2 4
2 5

5 3
7 5 7 7 1
1 2
2 3
3 4

comment)
자료구조 + 구현!!
"""
from collections import defaultdict

N, M = map(int, input().split())
W = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

count = 0
for i in range(len(W)):
    if not graph.get(i):  # 친분 관계가 없으면, 내가 최고!
        count += 1
    else:  # 친분 관계가 있으면, 내 친구들과 비교
        is_strongest = True
        for j in graph[i]:
            if W[i] <= W[j]:  # 친구 중 적어도 한명 보다 내가 강하지 못하면
                is_strongest = False
        if is_strongest:
            count += 1
print(count)
