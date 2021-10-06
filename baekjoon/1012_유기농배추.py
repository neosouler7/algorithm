import sys
sys.setrecursionlimit(100000)

def dfs(x, y, N, M, array, visited):
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if visited[nx][ny]:
            continue
        if array[nx][ny] == 0:
            continue
        dfs(nx, ny, N, M, array, visited)

def solution(N, M, array):
    count = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and array[i][j] == 1:
                dfs(i, j, N, M, array, visited)
                count += 1
    return count

T = int(input())
answer = list()
for t in range(T):
    M, N, K = map(int, input().split())
    array = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        array[b][a] = 1

    answer.append(solution(N, M, array))

for a in answer:
    print(a)

"""
dfs count!!

10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
"""