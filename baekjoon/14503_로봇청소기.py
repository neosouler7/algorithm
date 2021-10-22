"""

comment)
start + queue + dx/dy(d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽)
start = () x, y, direction, count(=1)

while queue:
    pop
    청소
    nx. ny : 왼쪽부터 방향 체크
     1.- 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
     2.- 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
     3.- 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
     4.- 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        => break
"""
N, M = map(int, input().split())
r, c, d = map(int, input().split())
array = list()
for _ in range(N):
    array.append(list(map(int, input().split())))  # wall: 1

from collections import deque

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]  # 북 / 동 / 남 / 서
    start = (r, c, d)  # x, y, direction
    queue = deque([start])
    count = 1
    array[r][c] = 2 # 시작점 청소 안해줘서 틀린거였음...........!!! + N, M 거꾸로 했음.....!! + 심심하면 아기상어 문제 풀어봥...

    while queue:
        x, y, direction = queue.popleft()
        for i in range(4):
            nd = (direction + 3) % 4
            nx, ny = x + dx[nd], y + dy[nd]

            # 1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            if 0 <= nx < N and 0 <= ny < M and array[nx][ny] == 0:
                array[nx][ny] = 2 # 방문 표시
                queue.append((nx, ny, nd))
                count += 1
                break
            # 3.네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            elif i == 3:
                bd = (direction + 2) % 4
                nx, ny = x + dx[bd], y + dy[bd]
                queue.append((nx, ny, direction))
                
                # 4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
                if array[nx][ny] == 1:
                    return count
                    
    
print(bfs())
