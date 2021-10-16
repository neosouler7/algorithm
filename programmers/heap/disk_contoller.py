"""
출처: 프로그래머스 > 힙 > 디스크 컨트롤러
내용: -
메모: 모르겠다
"""

import heapq

def solution(jobs):
    answer = 0
    now = 0
    i = 0
    start = -1
    heap = []

    for i in range(len(jobs)):
        # 현재 시점에 처리할 수 있는 작업 heap 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        # 처리할 작업이 있는 경우
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        # 없으면 time pass
        else:
            now += 1

    return answer // len(jobs)



jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
