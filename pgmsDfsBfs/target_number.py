"""
출처: 프로그래머스 > DFS/BFS > 타겟 넘버
내용: -
메모: -
"""

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))