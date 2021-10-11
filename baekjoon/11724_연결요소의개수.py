import sys
sys.setrecursionlimit(100000)
from collections import defaultdict


def dfs(node, graph, visited):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i, graph, visited)

def solution(N, graph):
    visited = [False] * (N+1)
    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i, graph, visited)
            count += 1
    return count

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(solution(N, graph))

"""
dfs count!


6 5
1 2
2 5
5 1
3 4
4 6
"""