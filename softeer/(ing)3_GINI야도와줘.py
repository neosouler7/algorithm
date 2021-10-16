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

R, C = map(int, input().split())
array = []
for _ in range(R):
    array.append(list(map(str, input())))

for i in range(R):
    for j in range(C):
        if array[i][j] == "H":
            start_x, start_y = i, j
        if array[i][j] == "W":
            end_x, end_y = i, j
        if array[i][j] == "*":
            rain_x, rain_y = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
queue = deque([(start_x, start_y, rain_x, rain_y)])

flag = False
answer = 0
visited = [[False for _ in range(C)] for _ in range(R)]
visited_r = [[False for _ in range(C)] for _ in range(R)]
while queue:
    x, y, rx, ry = queue.popleft()  # me, rain
    if x == end_x and y == end_y:
        flag = True
        break

    for i in range(4):  # 태범
        nx, ny = x + dx[i], y + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if visited[nx][ny]:
            continue

        rain = []
        if rx >= 0 and ry >= 0:  # 소나기가 있을때만(소멸될 수 있으므로_)
            for j in range(4):
                nrx, nry = rx + dx[j], ry + dy[j]
                if nrx >= R or nrx < 0 or nry >= C or nry < 0:
                    continue
                if visited_r[nrx][nry]:
                    continue
                if array[nrx][nry] == "H":  # 소나기는 강과 태범이의 집에 옮겨지지 않는다. 
                    continue
                if array[nrx][nry] == "X":  # (소나기는 강으로 가면 소멸)
                    break

                visited_r[nrx][nry] = True
                array[nrx][nry] = "*"  # 소나기 이동
                rain.append((nrx, nry))  # 가능한 소나기 조합 append

        if array[nx][ny] in [".", "W"]:  # 비어 있거나 세차장이면 움직이고
            visited[nx][ny] = True
            answer += 1

            rain = list(set(rain))  # 소나기 중복 제거
            if len(rain) == 0:
                queue.append((nx, ny, -1, -1))  # 소나기 소멸
            else:
                for r in rain:
                    queue.append((nx, ny, r[0], r[1]))

if flag:
    print(answer)
else:
    print("FAIL")
