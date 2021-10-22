"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=411

0,0을 기준으로 bfs를 돌린다.
이 때 이동은 0 따라 하고, 움직이는 것과 별개로 상하좌우에 1이면 그 값을 +1 한다.
큐 한번 쫙 돌면, >=2 이상인 것들 0으로 처리.

그리고 이걸 몇번 반복했는지

comment)
테스크 케이스 하나가 말썽이었는데 초기값 문제였음!!!
1 기준으로는 dfs 예상되지만, 0 기준으로 bfs를 돌아야 내부 얼음을 고려할 수 있다!

"""


N, M = map(int, input().split())
array = list()
for _ in range(N):
    array.append(list(map(int, input().split())))

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
zero_flag = True
for i in range(N):
    for j in range(M):
        if array[i][j] != 0:
            zero_flag = False
            break
if not zero_flag:
    while True:
        queue = deque([(0, 0)])
        visited = [[False for _ in range(M)] for _ in range(N)]  # repeat every time

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= N or nx < 0 or ny >=M or ny < 0:
                    continue
                if visited[nx][ny]:
                    continue
                
                if array[nx][ny] > 0:  # 인접 변 카운트
                    array[nx][ny] += 1

                if array[nx][ny] == 0:  # 0 이면 이동!
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        for i in range(N):
            for j in range(M):
                if array[i][j] >= 3:  # 녹을 대상 녹이고
                    array[i][j] = 0
                elif array[i][j] == 2:  # 대상 아니면 다시 얼음으로 바꿔줌
                    array[i][j] = 1
        count += 1

        finish_flag = True
        for i in range(N):
            for j in range(M):
                if array[i][j] != 0:
                    finish_flag = False
                    break
        if finish_flag:
            break

print(count)
