from collections import deque

def solution(N, K):
    visited = [False] * 100001
    dx = [-1, 1, 0]
    time = 0
    start = N
    queue = deque([(start, 0)])
    while queue:
        current, current_time = queue.popleft()
        time = max(time, current_time)
        if current == K:
            break

        visited[current] = True

        dx[2] = current
        for x in dx:
            nx = current + x
            if nx < 0 or nx > 100000:
                continue
            if not visited[nx]:
                visited[nx] = True
                queue.append((nx, current_time+1)) 
    return time

N, K = map(int, input().split())
print(solution(N, K))

"""
최단시간 BFS!!!

5 17
"""