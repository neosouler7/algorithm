"""
comment)
array of bool 형태의 visited가 익숙하긴 하지만,
경우에 따라서 여러 정보 조합의 set으로 처리해야하는 경우도 있음. 

"""
from collections import deque

def solution(n, m, array):
    # visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited = set([(0, 0, 1)])  # x, y, wall_hit
    start = [[0, 0, 1, 0]]  # x, y, distance, wall_hit
    queue = deque(start)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y, distance, wall_hit = queue.popleft()
        # visited[x][y][wall_hit] = True

        if x == n-1 and y == m-1:
            return distance

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if array[nx][ny] == 0 and not (nx, ny, wall_hit) in visited:
                queue.append([nx, ny, distance+1, wall_hit])
                visited.add((nx, ny, wall_hit))
            if array[nx][ny] == 1 and wall_hit == 0 and not (nx, ny, wall_hit+1) in visited:
                queue.append([nx, ny, distance+1, wall_hit+1])
                visited.add((nx, ny, wall_hit+1))

    return -1


n, m = map(int, input().split())
array = list()
for i in range(n):
    array.append(list(map(int, input())))

print(solution(n, m, array))

"""
6 4
0100
1110
1000
0000
0111
0000
"""