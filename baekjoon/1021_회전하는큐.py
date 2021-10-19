from collections import deque
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
target = list(map(int, sys.stdin.readline().rstrip().split()))

queue = deque([i for i in range(1, N+1)])
answer = 0
while queue:
    if len(target) == 0:
        break
    if target[0] == queue[0]:
        _ = queue.popleft()
        del target[0]
        continue

    distance = 0
    for j in range(len(queue)):
        if target[0] == queue[j]:
            distance = j

    if distance <= int(len(queue) / 2):  # right
        a = queue.popleft()
        queue.append(a)
    else:
        a = queue.pop()
        queue.appendleft(a)  # left
    answer += 1
print(answer)