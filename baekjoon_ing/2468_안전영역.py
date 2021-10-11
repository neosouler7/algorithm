import sys
sys.setrecursionlimit(100000)
from copy import deepcopy

def dfs(x, y):
    # visited[x][y] = True
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        # if visited[nx][ny]:
        #     continue
        if array[nx][ny] > height:
            dfs(nx, ny)


N = int(sys.stdin.readline())
array = list()
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

max_height = max(map(max, array))
max_count = 1
for height in range(1, max_height+1):
    # temp_array = deepcopy(array)
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] > height:
                dfs(i, j)
                count += 1
    max_count = max(max_count, count)
    # print(f'max: {max_count} | min({min_val}) max({max_val}) | height: {height} | count: {count}')

print(max_count)

"""
바꾸고, dfs!

5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""