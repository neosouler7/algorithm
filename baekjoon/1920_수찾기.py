import sys

N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
target = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(M):
    if target[i] in array:
        print("1")
    else:
        print("0")
