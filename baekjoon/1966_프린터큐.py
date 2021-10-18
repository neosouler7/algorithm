"""
4 2
1 2 3 4

-> 2
"""
import sys
from collections import deque

for _ in range(int(input())):
    N, M = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    array = []
    for i, t in enumerate(temp):
        array.append((i, t))
    temp.sort(reverse=True)

    max_importance = max(temp)
    answer = 0
    queue = deque(array)  # index, importance
    while queue:
        index, importance = queue.popleft()
        if importance < max_importance:  # 더 높은 우선순위 있으므로 뒤로
            queue.append((index, importance))
        else:  # 출력!
            answer += 1
            if index == M:  # 대상!
                print(answer)
                break
            max_importance = temp[answer]
