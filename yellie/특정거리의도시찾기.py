"""
출처: yellie > DFS/BFS > 특정 거리의 도시 찾기
내용: -
메모: 황서연 천재!!
"""
from collections import defaultdict, deque
import sys

INF = sys.maxsize

def solution(n, m, k, x, graph):
    visited = [False] * (n+1)
    dist = [INF] * (n+1)
    queue = deque([[x, 0]])

    while queue:
        node, distance = queue.popleft()
        dist[node] = min(dist[node], distance)
        visited[node] = True

        for i in graph[node]:
            if not visited[i]:
                queue.append([i, distance+1])

    is_valid = False
    for node in range(1, n+1):
        if dist[node] == k:
            is_valid = True
            print(node)
    
    if not is_valid:
        print(-1)
    


n, m, k, x = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

solution(n, m, k, x, graph)
"""
4 4 2 1
1 2
1 3
2 3
2 4


4 3 2 1
1 2 
1 3
1 4

4 4 1 1 
1 2 
1 3
2 3
2 4 
"""