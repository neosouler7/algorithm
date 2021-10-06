from collections import defaultdict


count = 0
def dfs(N, graph, visited):
    visited[N] = True
    global count
    count += 1
    for i in graph[N]:
        if not visited[i]:
            dfs(i, graph, visited)

N = int(input())  # number of node
K = int(input())  # number of edge
graph = defaultdict(list)
for i in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, graph, [False] * (N+1))
print(count-1)

"""
graph + start + dfs count !!!

7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""