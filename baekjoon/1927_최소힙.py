import heapq
import sys
heap = []
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        b = heapq.heappop(heap) if len(heap) > 0 else 0
        print(b)
    else:
        heapq.heappush(heap, a)