from collections import Counter
import sys
N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
counter = Counter(array)

M = int(sys.stdin.readline().rstrip())
target = list(map(int, sys.stdin.readline().rstrip().split()))

answer = [str(counter.get(t, 0)) for t in target]
print(*answer)