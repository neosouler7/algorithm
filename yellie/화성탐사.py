"""
출처: 이코테 > 최단경로 > 화성탐사
내용: -
메모: -
"""

import heapq
import sys
INF = sys.maxsize

def solution(N, array):
    distance = [[INF for _ in range(N)] for _ in range(N)]
    start = (array[0][0], 0, 0)  # cost, x, y

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = [start]
    while heap:
        cost, x, y = heapq.heappop(heap)
        if distance[x][y] < cost:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or nx < 0 or ny >=N or ny < 0:
                continue


            new_cost = cost + array[nx][ny]
            if new_cost < distance[nx][ny]:
                heapq.heappush(heap, (new_cost, nx, ny))
                distance[nx][ny] = new_cost
    
    print(distance[N-1][N-1])


T = int(input())
for j in range(T):
    N = int(input())
    array = list()
    for i in range(N):
        array.append(list(map(int, input().split())))
    solution(N, array)


"""
3
3
5 5 4
3 9 1 
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""