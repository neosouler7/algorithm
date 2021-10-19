import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
listen = []
for _ in range(N):
    listen.append(sys.stdin.readline().rstrip())
look = []
for _ in range(M):
    look.append(sys.stdin.readline().rstrip())

answer = list(set(listen) & set(look))
answer.sort()
print(len(answer))
for a in answer:
    print(a)