"""
3
1 3
2 4
3 5

6
3 5
1 3
1 2
1 4
2 4
2 3

"""
import heapq

N = int(input())
lessons = []
for _ in range(N):
    a, b = map(int, input().split())
    lessons.append((a, b))

lessons = sorted(lessons, key=lambda x: x[0])  # 시작 시간 기준

q = []
for l in lessons:
    if q and q[0] <= l[0]:  # 2. 이전의 끝나는 vs 지금의 시작
        heapq.heappop(q)
    heapq.heappush(q, l[1])  # 1. 끝나는 시간을 넣고
    
print(len(q))