"""
출처: 프로그래머스 > 힙 > 더 맵게
내용: -
메모: 순서가 보장되어야 하므로 이에 적합한 자료구조를 사용하자~
"""

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while True:
        if scoville[0] > K:
            break

        # 문제에 "모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다." 이 조건도 고려해야돼요
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]	
K = 7
print(solution(scoville, K))
