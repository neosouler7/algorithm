"""
출처: 프로그래머스 > 스택/큐 > 기능개발
내용: zip 및 deque 활용
메모: popleft 활용한 기본적인 조건식 
"""

from collections import deque
import math

def solution(progresses, speeds):
    days = deque()
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100-p) / s))

    answer = []
    count, d = 0, days[0]
    while days:
        n = days.popleft() 
        if d < n:
            answer.append(count)
            count = 0
            d = n
        count += 1
    answer.append(count)
    return answer

    
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))