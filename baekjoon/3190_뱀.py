"""
comment)
queue 안에 어떠한 정보를 함께 담을지!
: 좌표, 방향, 시간, 몸

그 시간대에 방향이 바뀌는지도 봐야해 -> 방향을 결정하고

죽는 조건 2개(벽 or 몸) -> break

그 방향으로 사과가 있는지 확인 (몸 전체를 들고 다닌다)
    있으면, nx/ny 넣어준다
    없으면, nx/ny 넣어준다 + 꼬리를 없앤다
    시간 ++ 

"""

N = int(input())
K = int(input())
apple = [[False for _ in range(N)] for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    apple[a-1][b-1] = True

L = int(input()) 
snake_move = dict()
for i in range(L):
    a, b = map(str, input().split())
    snake_move[a] = b


from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]  # 동 북 서 남

start = (0, 0, 0, 0, [(0, 0)])  # x, y, direction, time, body
queue = deque([start])

while queue:
    x, y, direction, time, body = queue.popleft()

    # 방향 및 다음 칸 결정
    if snake_move.get(str(time)):  
        if snake_move.get(str(time)) == "D":
            direction = (direction + 3) % 4
        if snake_move.get(str(time)) == "L":
            direction = (direction + 1) % 4
    nx, ny = x + dx[direction], y + dy[direction]

    # 죽는 조건(벽 or 몸)
    if nx >= N or nx < 0 or ny >= N or ny < 0:
        print(time+1)
        break
    if (nx, ny) in body:
        print(time+1)
        break

    # 사과가 없으면 앞에꺼 뺀다
    if not apple[nx][ny]:
        body = body[1:]
    
    # 한번 먹은 사과는 없다.
    apple[nx][ny] = False
    
    next = (nx, ny, direction, time+1, body + [(nx, ny)])  # x, y, direction, time, body
    queue.append(next)
