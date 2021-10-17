"""
4 3
####
#*@.
####

'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불

comment)
75번째 줄 if fire_visited[nx][ny] > -1 이 빠져있었음 ㅠ.ㅠ

"""
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    array = [list(map(str, input())) for _ in range(h)]

    fire = []
    fire_visited = [[-1 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if array[i][j] == "@":
                start_x, start_y = i, j
            if array[i][j] == "*":
                fire_visited[i][j] = 0
                fire.append((i, j, 0))  # x, y, time
    
    fire_queue = deque(fire)
    while fire_queue:
        x, y, time = fire_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            ntime = time + 1
            if nx >= h or nx < 0 or ny >= w or ny < 0:
                continue
            if fire_visited[nx][ny] > -1:
                continue        
            if array[nx][ny] == "#":  # 벽에는 불이 붙지 않는다.
                continue
            fire_visited[nx][ny] = ntime
            fire_queue.append((nx, ny, ntime))

    queue = deque([(start_x, start_y, 0)])  # x, y, time
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    answer = 0

    # 상근이가 애초에 탈출구에서 시작한다면
    if (start_x == 0 or start_x == h-1 or start_y == 0 or start_y == w-1):
        answer = 1
        print(answer)
        continue

    while queue:
        x, y, time = queue.popleft()
        if array[x][y] == "." and (x == 0 or x == h-1 or y == 0 or y == w-1):
            answer = time + 1
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            ntime = time + 1
            if nx >= h or nx < 0 or ny >= w or ny < 0:
                continue
            if visited[nx][ny] > -1:
                continue  
            if array[nx][ny] == "#":  # 상근이는 벽을 통과할 수 없고
                continue
            if fire_visited[nx][ny] > -1 and fire_visited[nx][ny] <= ntime:  # 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 
                continue
            visited[nx][ny] = ntime
            queue.append((nx, ny, ntime))


    if answer > 0:
        print(answer)
    else:
        print("IMPOSSIBLE")