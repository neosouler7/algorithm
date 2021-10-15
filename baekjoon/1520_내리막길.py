"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
"""

M, N = map(int, input().split())
array = []
for _ in range(M):
    array.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1

    if visited[x][y] == -1:
        visited[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= M or nx < 0 or ny >= N or ny < 0:
                continue

            if array[x][y] > array[nx][ny]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]

print(dfs(0, 0))