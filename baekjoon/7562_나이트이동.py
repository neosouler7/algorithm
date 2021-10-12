"""
8
0 0
7 0
"""


from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(I, X1, Y1, X2, Y2):
    visited = [[False for _ in range(I)] for _ in range(I)]
    visited[X1][Y1] = True
    start = (X1, Y1, 0)  # x, y, count
    queue = deque([start])
    while queue:
        x, y, count = queue.popleft()
        if x == X2 and y == Y2:
            return count
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= I or nx < 0 or ny >= I or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny, count + 1))



N = int(input())
for _ in range(N):
    I = int(input())
    X1, Y1 = map(int, input().split())
    X2, Y2 = map(int, input().split())
    print(bfs(I, X1, Y1, X2, Y2))