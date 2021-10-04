"""
출처: Softter > 장애물 인식 프로그램
내용: dfs 총 count + 각 count 
메모: -
"""

subcount = 0

def dfs(x, y, n, array, visited):
    visited[x][y] = 1
    global subcount
    subcount += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue

        if visited[nx][ny] == 1 or array[nx][ny] == 0:
            continue

        dfs(nx, ny, n, array, visited)

def solution(n, array):
    count, result = 0, list()
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and array[i][j] == 1:
                global subcount
                subcount = 0
                dfs(i, j, n, array, visited)
                count += 1
                result.append(subcount)
    
    print(count)
    result.sort()
    for r in result:
        print(r)


n = int(input())
array = list()
for i in range(n):
    array.append(list(map(int, input())))

solution(n, array)

"""
7
1110111
0110101
0110101
0000100
0110000
0111110
0110000
"""