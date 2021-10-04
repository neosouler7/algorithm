"""
출처: yellie > DFS/BFS > 음료수 얼려먹기
내용: -
메모: 황서연 천재!!
"""

def dfs(x, y, n, m, array, visited):
    visited[x][y] = 1

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if visited[nx][ny] == 1 or array[nx][ny] == 1:
            continue
        dfs(nx, ny, n, m, array, visited)


def solution(n, m, array):
    # bfs count!!
    count = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and array[i][j] == 0:
                dfs(i, j, n, m, array, visited)
                count += 1
    return count


n, m = map(int, input().split())
array = list()
for i in range(n):
    array.append(list(map(int, input())))

print(solution(n, m, array))


"""
4 5
00110
00011
11111
00000
"""