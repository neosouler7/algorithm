"""
comment)
dfs, bfs 로직이 메인함수에서 분리되는 경우
반드시 큰 틀을 먼저 설계할 것.
"""

N = int(input())
array = list()
for _ in range(N):
    array.append(list(map(int, input().split())))

init_x, init_y = 0, 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 9:
            array[i][j] = 0  # 상어 위치 파악 후 0으로
            init_x, init_y = i, j


# 3-2. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

from collections import deque
import heapq


def bfs(x, y, shark_size):
    visited = [[False for _ in range(N)] for _ in range(N)]
    heap = []  # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다
    start = (x, y, 0)
    queue = deque([start])
    while queue:
        x, y, distance = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if visited[nx][ny]:
                continue

            fish_size = array[nx][ny]
            if fish_size > shark_size:
                continue
            elif fish_size == shark_size or fish_size == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
            else:  # fish < shark -> eat!!!: 먹을 놈이니까 heap에 넣는다.
                visited[nx][ny] = True
                heapq.heappush(heap, (distance + 1, nx, ny, fish_size))

    return heap
            
eat = 0
time = 0
shark_size = 2
while True:
    fish_target = bfs(init_x, init_y, shark_size)
    if len(fish_target) == 0:  # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
        print(time)
        break
    
    distance, nx, ny, fish_size = fish_target[0]
    eat += 1
    array[nx][ny] = 0
    if eat == shark_size:
        eat = 0
        shark_size += 1
    time += distance

    init_x, init_y = nx, ny
   





















# while queue:
#     # 3-1. 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
#     queue = deque(sorted(queue))
#     for _ in range(len(queue)):
#         x, y = queue.popleft()

#         if array[x][y] != 0 and array[x][y] < size:  # eat!!!!!!!!!
#             array[x][y] = 0
#             eat += 1

#             if eat == size:
#                 size += 1
#                 eat = 0

#             queue = deque()
#             visited = [[False for _ in range(N)] for _ in range(N)]

#             answer = time  # 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지
#             eat_flag = True
        
#         # 3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다 -> bfs
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if nx >= N or nx < 0 or ny >= N or ny < 0:
#                 continue
#             if visited[nx][ny]:
#                 continue
#             if array[nx][ny] < size:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
        
#         if eat_flag:
#             eat_flag = False
#             break

#     time += 1

# print(answer)