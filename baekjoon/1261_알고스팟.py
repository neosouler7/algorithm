"""
comment)
bfs!

벽을 못 간다고 생각하지 말고,
1의 비용이 든다고 생각할 것
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
array = []
for _ in range(M):
    array.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[-1 for _ in range(N)] for _ in range(M)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
start = (0, 0)
queue = deque([start])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= M or nx < 0 or ny >= N or ny < 0:
            continue
        if visited[nx][ny] == -1:
            if array[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]
                queue.appendleft((nx, ny))
            elif array[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
print(visited[M-1][N-1])
