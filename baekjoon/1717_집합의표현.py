"""
comment)
구현 했으나, 타임아웃.
상호배타적인 집합(Disjoint Set) => union-find 알고리즘 
"""

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
parent = [i for i in range(N+1)]

def union(x, y):
    a, b = find(x), find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")

# import sys
# N, M = map(int, sys.stdin.readline().rstrip().split())
# target = []  # list of list
# for _ in range(M):
#     l = list(map(int, sys.stdin.readline().rstrip().split()))
#     if l[0] == 0:
#         if len(target) == 0:
#             target.append([l[1], l[2]])
#         else:
#             flag = True
#             for t in target:
#                 if l[1] in t:
#                     flag = False
#                     t.append(l[2])  # 기존 리스트 append
#             if flag:
#                 target.append([l[2]])  # 신규 리스트 append
#     elif l[0] == 1:
#         if l[1] == l[2]:
#             print('YES')
#             continue
#         else:
#             flag = True
#             for t in target:
#                 if l[1] in t and l[2] in t:
#                     flag = False
#                     print('YES')
#                     continue
#             if flag:
#                 print('NO')
