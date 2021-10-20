"""
comment)
다익스트라!
도착도시이면, 해당 비용 출력!
"""
import sys
from collections import defaultdict
import heapq
INF = sys.maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))  # from / cost, node
start, end = map(int, sys.stdin.readline().split())

def dijkstra():
    distance = [INF] * (N+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))  # cost, node
    while heap:
        cost, node = heapq.heappop(heap)
        if node == end:
            print(cost)
            break
        if distance[node] < cost:
            continue
        for i in graph[node]:
            new_cost, new_node = cost + i[0], i[1]
            if new_cost < distance[new_node]:
                distance[new_node] = new_cost
                heapq.heappush(heap, (new_cost, new_node))

dijkstra()
