"""
bfs count / subcount
"""
import sys
sys.setrecursionlimit(100000)


N, M, K = map(int, input().split())  # x, y change
array = [[False for _ in range(M)] for _ in range(N)]
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())  # x, y change
    for i in range(x1, x2):
        for j in range(y1, y2):
            array[i][j] = True

sub_count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    array[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if not array[nx][ny]:
            global sub_count
            sub_count += 1
            dfs(nx, ny)

def solution(M, N, array):
    count = 0
    count_list = []
    for i in range(N):
        for j in range(M):
            if not array[i][j]:
                global sub_count
                sub_count = 1
                dfs(i, j)
                count_list.append(sub_count)
                count += 1

    count_list.sort()
    return count, count_list

count, count_list = solution(M, N, array)
print(count)
print(' '.join([str(c) for c in count_list]))