"""
3 3
H.*
...
W..

https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=583

bfs

일단 소나기가 없다고 생각해보자 -> 짰음

태범이와 소나기는 독립적이지 않은가...
그러면 각 경우마다 또 돌아야할듯?
"""


# 소나기, 각 지점마다 몇초에 소나기가 지났는지
# 태범, 소나기 고려 bfs


R, C = map(int, input().split())
array = []
for _ in range(R):
    array.append(list(map(str, input())))

for i in range(R):
    for j in range(C):
        if array[i][j] == "W":
            start_x, start_y = i, j
        if array[i][j] == "H":
            end_x, end_y = i, j
        if array[i][j] == "*":
            rain_x, rain_y = i, j

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 소나기
rain_queue = deque([(rain_x, rain_y, 0)])
rain_visited = [[-1 for _ in range(C)] for _ in range(R)]  # 각 지점 별 언제 소나기가 있었는지
rain_visited[rain_x][rain_y] = 0
while rain_queue:
    x, y, rain_time = rain_queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if rain_visited[nx][ny] > -1:
            continue
        if array[nx][ny] in ["H", "W"]:  # 소나기 -> 집: 옮겨지지 않음
            continue
        if array[nx][ny] == "X":  # 소나기 -> 강: 소멸
            break
        
        rain_visited[nx][ny] = rain_time + 1
        rain_queue.append((nx, ny, rain_time + 1))

# for r in rain_visited:
#     print(r)

# 태범
def solution():
    queue = deque([(start_x, start_y, 0)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[start_x][start_y] = True
    while queue:
        x, y, time = queue.popleft()  # x, y, time

        if x == end_x and y == end_y:
            return time

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= R or nx < 0 or ny >= C or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            if rain_visited[nx][ny] == time + 1:  # 가야할 시점/장소에 소나기가 있다면!
                continue

            if array[nx][ny] in [".", "H"]:  # 갈 수 있는 곳에 대해서만
                visited[nx][ny] = True
                queue.append((nx, ny, time + 1))

    return "FAIL"

print(solution())
