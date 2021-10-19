import sys
answer = ''
for s in sys.stdin.readline().rstrip().split("-"):
    answer += s[0]
print(answer)