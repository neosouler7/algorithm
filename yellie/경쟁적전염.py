"""
출처: 이코테 > dfs&bfs > 경쟁적 전염
내용: -
메모: -
"""

from collections import deque
from operator import itemgetter


def solution(array, n, k, s, tx, ty):
    virus = []
    for i in range(n):
        for j in range(n):
            if array[i][j] > 0:
                virus.append((i, j, array[i][j], 0))
    
    virus = sorted(virus, key=itemgetter(2))

    visited = [[False for _ in range(n)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque(virus)
    while queue:
        x, y, power, second = queue.popleft()
        if second == s:
            break

        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[nx][ny]:
                continue
            
            if array[nx][ny] == 0:
                array[nx][ny] = power
                queue.append((nx, ny, power, second + 1))
        
    return array[tx-1][ty-1]



n, k = map(int, input().split())
array = list()
for i in range(n):
    array.append(list(map(int, input().split())))
s, tx, ty = list(map(int, input().split()))

print(solution(array, n, k, s, tx, ty))

"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3 
1 0 2
0 0 0
3 0 0
1 2 2

4 2
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
3 3 2


3 3
1 0 1
3 0 0
0 0 2
2 1 1
"""