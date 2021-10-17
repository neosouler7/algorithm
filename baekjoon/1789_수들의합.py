S = int(input())
N = 1
while True:
    temp = N * (N+1) / 2
    if temp > S:
        break
    N += 1
print(N-1)