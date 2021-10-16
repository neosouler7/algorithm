"""
출처: 프로그래머스 > 스택/큐 > 프린터
내용: queue + 기본적인 연산. 최초 위치가 보장되어야 함 주의!
메모: 굿 접근
"""

from collections import deque
from operator import itemgetter

def solution(priorities, location):
    answer = 0
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    while True:
        item = queue.popleft()
        if len(queue) > 0 and max(queue, key=itemgetter(0))[0] > item[0]:
            queue.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

priorities = [2, 1, 3, 2]
location = 2 
print(solution(priorities, location))
