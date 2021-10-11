from collections import defaultdict, deque
import sys

dfs_list = []
bfs_list = []

def dfs(V, graph, visited):
    visited[V] = True
    global dfs_list
    dfs_list.append(V)
    # print(V, end = " ")
    for i in graph[V]:
        if not visited[i]:
            dfs(i, graph, visited)


def bfs(V, graph, visited):
    start = V
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visited[node] = True
        global bfs_list
        bfs_list.append(node)
        # print(node, end = " ")

        if all(visited[1:]):
            break

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)

N, M, V = map(int, sys.stdin.readline().split())
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

dfs(V, graph, visited_dfs)
# print()
bfs(V, graph, visited_bfs)

print(*dfs_list)
print(*bfs_list)

# print(graph)
"""
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1
"""


