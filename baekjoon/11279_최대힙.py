import heapq
import sys
heap = []
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(heap) > 0:
            b = heapq.heappop(heap)
            print(b[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-a, a))