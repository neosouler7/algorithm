"""
출처: 이코테 > 최단경로 > 전보
내용: -
메모: -
"""

from collections import defaultdict
import sys
INF = sys.maxsize
import heapq

def solution(N, M, C, graph):
    distance = [INF] * (N+1)
    heap = [(0, C)]  # cost, node (MIN-HEAP)

    while heap:
        cost, node = heapq.heappop(heap)
        if distance[node] < cost:
            continue

        distance[node] = cost

        for i in graph[node]:
            if distance[i[0]] > cost + i[1]:  # 만약 갈 곳도 미리 비교해서 too much 이면 안 넣어준다.
                heapq.heappush(heap, (cost + i[1], i[0]))

    count, max_val = 0, 0
    for d in distance:
        if d == INF or d == 0:
            continue
        count += 1
        max_val = max(max_val, d)

    print(f'{count} {max_val}')

N, M, C = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))


solution(N, M, C, graph)

"""
1 2 4
1 : (2, 4)  # from: (to, cost)
"""

"""
3 2 1
1 2 4
1 3 2
"""