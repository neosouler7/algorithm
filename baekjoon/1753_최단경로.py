import sys
sys.setrecursionlimit(1000000)

from collections import defaultdict
import heapq
import sys
INF = sys.maxsize

def solution(V, K, graph):
    distance = [INF] * (V+1)
    distance[K] = 0
    heap = []
    heapq.heappush(heap, (0, K))  # cost, node

    while heap:
        cost, node = heapq.heappop(heap)
        if distance[node] < cost:
            continue


        for i in graph[node]:
            next_cost = cost + i[0]
            next_node = i[1]
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
    
    for d in distance[1:]:
        val = "INF" if d == INF else d
        sys.stdout.write(str(val) + "\n")


V, E = map(int, sys.stdin.readline().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # from / weight, to

solution(V, K, graph)



"""
다익스트라!!

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""