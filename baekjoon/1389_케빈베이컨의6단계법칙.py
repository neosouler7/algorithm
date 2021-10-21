"""
comment)
bfs!

"""
from collections import defaultdict, deque
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0] * (N+1)
for i in range(1, N+1):
    start = (i, 0)  # user, count
    visited = [-1] * (N+1)
    visited[i] = 1
    queue = deque([start])

    while queue:
        user, count = queue.popleft()
        for j in graph[user]:
            if visited[j] == -1:
                visited[j] = count + 1
                queue.append((j, count + 1))

    answer[i] = sum(visited)

min_idx = 0
min_val = sys.maxsize
for i in range(1, N+1):
    if answer[i] < min_val:
        min_val = answer[i]
        min_idx = i
print(min_idx)