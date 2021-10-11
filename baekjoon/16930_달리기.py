from collections import deque
import sys
INF = sys.maxsize


N, M, K = map(int, input().split())
array = list()
for _ in range(N):
    array.append(list(map(str, input())))
X1, Y1, X2, Y2 = map(int, input().split())

distance = [[INF for _ in range(M)] for _ in range(N)]
start = [X1-1, Y1-1, 0]
queue = deque([start])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, cost = queue.popleft()
    distance[x][y] = cost

    if x == X2-1 and y == Y2-1:
        break

    for i in range(4):
        for k in range(1, K+1):
            nx, ny = x + dx[i]*k, y + dy[i]*k
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            
            if array[nx][ny] == "#":
                break

            if distance[nx][ny] <= distance[x][y]:  # 이미 갔던 경우...는 안 간다
                break

            new_cost = cost + 1

            if new_cost < distance[nx][ny]:
                distance[nx][ny] = new_cost
                queue.append([nx, ny, new_cost])

print(-1 if distance[X2-1][Y2-1] == INF else distance[X2-1][Y2-1])







"""
3 4 4
....
###.
....
1 1 3 1
"""