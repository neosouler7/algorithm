"""
출처: 백준 > dfs&bfs > 적록색약
내용: -
메모: -
"""

def dfs(x, y, n, array, visited):
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[nx][ny]:
            continue

        if array[x][y] == array[nx][ny]:
             dfs(nx, ny, n, array, visited)


import sys
sys.setrecursionlimit(100000)
from copy import deepcopy

def solution(n, array):
    visited_normal = [[False for _ in range(n)] for _ in range(n)]
    visited_unnormal = [[False for _ in range(n)] for _ in range(n)]

    # dfs_normal
    count_normal = 0
    for i in range(n):
        for j in range(n):
            if not visited_normal[i][j]:
                dfs(i, j, n, array, visited_normal)
                count_normal += 1

    # dfs_unnormal
    array_unnormal = deepcopy(array)
    count_unnormal = 0
    for i in range(n):
        for j in range(n):
            if array_unnormal[i][j] == "G":
                array_unnormal[i][j] = "R"
    for i in range(n):
        for j in range(n):
            if not visited_unnormal[i][j]:
                dfs(i, j, n, array_unnormal, visited_unnormal)
                count_unnormal += 1

    print(f'{count_normal} {count_unnormal}')
                

n = int(input())
array = list()
for i in range(n):
    array.append(list(map(str, input())))

solution(n, array)

"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""