"""
출처: 삼성 > 연구소
내용: -
메모: -
"""

zero_count = 0

def dfs(x, y, n, m, array, visited):
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0 or visited[nx][ny]:
            continue
        
        if array[nx][ny] == 0:
            array[nx][ny] = 2
            dfs(nx, ny, n, m, array, visited)


def dfs_zero(x, y, n, m, array, visited):
    visited[x][y] = True
    global zero_count
    zero_count += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0 or visited[nx][ny]:
            continue

        if array[nx][ny] == 0:
            dfs_zero(nx, ny, n, m, array, visited)
        

import itertools
from copy import deepcopy

def subsolution(array, n, m):
    global zero_count
    zero_count = 0
    # 2를 찾아서 근접이 0인 것들을 2로 바꾼다.
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and array[i][j] == 2:
                dfs(i, j, n, m, array, visited)
    
    # dfs를 돌면서 0의 개수를 찾는다.
    visited_zero = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited_zero[i][j] and array[i][j] == 0:
                
                dfs_zero(i, j, n, m, array, visited_zero)
    
    return zero_count


def solution(n, m, array):
    zero_coord = list()
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                zero_coord.append([i, j])

    comb = itertools.combinations(zero_coord, 3)

    current_subcount = 0
    for com in comb:
        array_copy = deepcopy(array)
        c1, c2, c3 = com
        array_copy[c1[0]][c1[1]] = 1
        array_copy[c2[0]][c2[1]] = 1
        array_copy[c3[0]][c3[1]] = 1

        current_subcount = max(subsolution(array_copy, n, m), current_subcount)

    return current_subcount


n, m = map(int, input().split())
array = list()
for _ in range(n):
    array.append(list(map(int, input().split())))

print(solution(n, m, array))

"""
7 7
2100110
1010120
0110100
0100010
0000011
0100000
0100000


7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
000000
100002
111002
000002

8 8
20000002
20000002
20000002
20000002
20000002
00000000
00000000
00000000
"""