"""
3 3
50 50
40 40
10 30
60 76
18 28
22 50

comment)
"""

N, M = map(int, input().split())
master, current = list(), list()

temp = 0
for i in range(N):
    a, b = map(int, input().split())
    if i == 0:
        master.append((0, a, b))
        temp += a
    elif i == N-1:
        master.append((temp, 100, b))
    else:
        master.append((temp, temp+a, b))
        temp += a

temp = 0
for i in range(M):
    a, b = map(int, input().split())
    if i == 0:
        current.append((0, a, b))
        temp += a
    elif i == N-1:
        current.append((temp, 100, b))
    else:
        current.append((temp, temp+a, b))
        temp += a

def get_speed(target, t):
    for m in target:
        start, end, speed = m
        if start <= t < end:
            return speed

answer = 0
for i in range(100):
    answer = max(answer, get_speed(current, i) - get_speed(master, i))

if answer < 0:
    print(0)
else:
    print(answer)
