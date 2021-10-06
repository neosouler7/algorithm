from collections import deque


def solution(N, M, array):
    visited = [[False for _ in range(M)] for _ in range(N)]
    tomato = list()
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                tomato.append((i, j, 0))  # x, y, time
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque(tomato)
    total_time = 0
    while queue:
        x, y, time = queue.popleft()
        visited[x][y] = True
        total_time = max(total_time, time)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            if array[nx][ny] == 0:
                array[nx][ny] = 1
                queue.append((nx, ny, time+1))

    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                return -1
    return total_time

M, N = map(int, input().split())
array = list()
for _ in range(N):
    array.append(list(map(int, input().split())))
print(solution(N, M, array))

"""
최소일수 !!! BFS

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""