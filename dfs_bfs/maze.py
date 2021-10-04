n, m = map(int, input().split())

graph = list()
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >=m :
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[nx-1][ny-1]


print(bfs(0, 0))



"""
5 6
101010
111111
000001
111111
111111
"""
