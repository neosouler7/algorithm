"""
(7, 3)
1 2 3 4 5 6 7
    1
          2 
  3         4
        5
6     7


3 6 2 7 5 1 4
"""
from collections import deque
N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
answer = []
i = 1
while queue:
    x = queue.popleft()
    if i < K:
        queue.append(x)
    if i == K:
        answer.append(x)
        i = 1
        continue
    i += 1
print(f'<{", ".join(str(a) for a in answer)}>')