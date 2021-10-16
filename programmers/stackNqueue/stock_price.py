"""
출처: 프로그래머스 > 스택/큐 > 주식 가격
내용: 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
     가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
메모: queue 활용하여 시간복잡도를 낮춘다
"""

from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        count = 0
        for q in queue:
            count += 1
            if price > q:
                break
        answer.append(count)
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))