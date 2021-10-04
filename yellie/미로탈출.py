"""
출처: yellie > DFS/BFS > 미로탈출
내용: -
메모: 황서연 천재!!
"""

from collections import deque

def solution(n, m, array):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 1)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        val = queue.popleft()
        x, y, distance = val[0], val[1], val[2]
        if x == n-1 and y == m-1:
            return distance
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >=m or ny < 0 or visited[nx][ny]:
                continue
            
            if array[nx][ny] == 1:
                queue.append((nx, ny, distance+1))



n, m = map(int, input().split())
array = list()
for i in range(n):
    array.append(list(map(int, input())))

print(solution(n, m, array))

"""
그래프 탐색을 해야할 것이고 최단거리네~~~ 
근데 가중치가 다 같구나!!! 그럼 bfs!!!

5 6
101010
111111
000001
111111
111111
"""