import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())
array = list()
for _ in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def bfs(m, n):
    # visited = [[False for _ in range(N)] for _ in range(N)]
    start = (m, n)
    queue = deque([start])
    # change_target = list([start])
    change_target = set([start])
    path_sum = array[m][n]  # critical
    # visited[m][n] = True  # critical
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            # if visited[nx][ny]:
            #     continue
            if (nx, ny) in change_target:
                continue

            if L <= abs(array[x][y] - array[nx][ny]) <= R:
                # visited[nx][ny] = True
                queue.append((nx, ny))
                path_sum += array[nx][ny]
                # change_target.append((nx, ny))  # nx, ny
                change_target.add((nx, ny))

    return change_target, path_sum

time = 0
while True:
    change_target = []
    for i in range(N):
        for j in range(N):
            path, path_sum = bfs(i, j)
            if path_sum > array[i][j]:
                change_target.append((path, path_sum))

    if len(change_target) == 0:
        print(time)
        break

    for c in change_target:
        path, path_sum = c
        for (x, y) in path:
            array[x][y] = path_sum // len(path)
        
    time += 1
