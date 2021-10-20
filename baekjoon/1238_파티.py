"""
dijkstra!!
N -> X -> N
start, end가 다른 두 번의 다익스트라 돌려야 하고,
answer 배열에 각각 엎어친다.
"""
import sys
INF = sys.maxsize
from collections import defaultdict
import heapq

N, M, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))  # from / cost, to
answer = [0] * (N+1) 

for n in range(1, N+1):
    distance = [INF] * (N+1)
    distance[n] = 0
    heap = []
    heapq.heappush(heap, (0, n))  # cost, node
    while heap:
        cost, node = heapq.heappop(heap)
        if node == X:  # X네 집에 놀러가자!
            answer[n] += cost
            break
        if distance[node] < cost:
            continue
        for i in graph[node]:
            new_cost, new_node = cost + i[0], i[1]
            if new_cost < distance[new_node]:
                distance[new_node] = new_cost
                heapq.heappush(heap, (new_cost, new_node))

for n in range(1, N+1):
    distance = [INF] * (N+1)
    distance[X] = 0
    heap = []
    heapq.heappush(heap, (0, X))  # cost, node
    while heap:
        cost, node = heapq.heappop(heap)
        if node == n:  # 각자 집에 돌아가자!
            answer[n] += cost
            break
        if distance[node] < cost:
            continue
        for i in graph[node]:
            new_cost, new_node = cost + i[0], i[1]
            if new_cost < distance[new_node]:
                distance[new_node] = new_cost
                heapq.heappush(heap, (new_cost, new_node))

print(max(answer[1:]))