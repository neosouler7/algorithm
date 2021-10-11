import sys
sys.setrecursionlimit(100000)

def dfs(W, H, x, y, array, visited):
    visited[x][y] = True
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= H or nx < 0 or ny >= W or ny < 0:
            continue
        if visited[nx][ny]:
            continue
        if array[nx][ny] == 1:
            dfs(W, H, nx, ny, array, visited)


def solution(W, H, array):
    visited = [[False for _ in range(W)] for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and array[i][j] == 1:
                dfs(W, H, i, j, array, visited)
                count += 1
    return count

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    array = list()
    for i in range(H):
        array.append(list(map(int, input().split())))

    print(solution(W, H, array))

"""
3 2
1 1 1
1 1 1
"""