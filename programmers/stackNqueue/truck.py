"""
출처: 프로그래머스 > 스택/큐 > 트럭
내용: -
메모: -
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_count = len(truck_weights)
    yet, ing, finished = deque(truck_weights), deque(), deque()

    while len(finished) == truck_count:
        temp_yet = truck_weights[0]
        if len(ing) + 1 > bridge_length:  # 하나 추가했는데 길이 초과하면 pass
            continue 
        if sum(ing) + temp_yet > weight:  # 하나 추가했는데 무게 초과하면 pass
            continue
        
        truck = yet.popleft()
        ing.append(truck)

        
        pass


    return answer



bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

print(solution(bridge_length, weight, truck_weights))
