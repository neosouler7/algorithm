"""
3 3
H.*
...
W..

3 3
H.*
.X.
W..

https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=583

bfs

"태범이가 최단경로로 움직이는데, 움직이려는 곳에 그 시간에 소나기가 있으면 피해간다."
1. 각 좌표별 소나기가 위치하는 시간
    : 소나기는 강과 태범이의 집에 옮겨지지 않는다. (소나기는 강으로 가면 소멸)
2. 소나기가 없다고 가정하고, 태범이 홀로 이동
3. 2번 && 1번

"""

R, C = map(int, input().split())
array = []
for _ in range(R):
    array.append(list(map(str, input())))

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rain = []
rain_visited = [[-1 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if array[i][j] == "*":  # rain
            rain_visited[i][j] = 0
            rain.append((i, j, 0))  # 소나기는 여러개일 수 있음
        if array[i][j] == "W":  # 세차장(시작)
            start_x, start_y = i, j
        if array[i][j] == "H":  # 집(도착)
            end_x, end_y = i, j


rain_queue = deque(rain)
while rain_queue:
    x, y, time = rain_queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        new_time = time + 1
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if rain_visited[nx][ny] > -1:
            continue
        if array[nx][ny] == "X":  # 강으로 가면 소멸
            continue
        if array[nx][ny] == "H":  # 태범 집 이동 불가
            continue
        if array[nx][ny] in [".", "W"]:  # 비어 있거나 세차장이면
            rain_visited[nx][ny] = new_time
            rain_queue.append((nx, ny, new_time))

# for r in rain_visited:
#     print(r)

queue = deque([(start_x, start_y, 0)])  # x, y, time (태범)
visited = [[-1 for _ in range(C)] for _ in range(R)]
visited[start_x][start_y] = 0  # 0초
answer = 0
while queue:
    x, y, time = queue.popleft()
    if x == end_x and y == end_y:  # 집 도착
        answer = time
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        new_time = time + 1
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if visited[nx][ny] > -1:
            continue
        if array[nx][ny] == "X":  # 강
            continue
        if rain_visited[nx][ny] > -1 and rain_visited[nx][ny] == new_time:  # 가려는 곳, 시간에 소나기가 있다면! => 소나기가 이미 지나간 곳은 갈 수 없다
            continue
        if array[nx][ny] in [".", "H"]:  # 비어 있거나 집이면
            visited[nx][ny] = new_time
            queue.append((nx, ny, new_time))

if answer > 0:
    print(answer)
else:
    print("FAIL")
