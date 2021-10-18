import sys
answer = []
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a != 0:
        answer.append(a)
    else:
        answer.pop()
print(sum(answer))