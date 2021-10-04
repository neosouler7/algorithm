import sys
sys.setrecursionlimit(100000)


def factorial(N):
    if N == 0:
        return 1
    cache = [0] * (N+1)
    idx = 0
    cache[idx] = 1
    while True:
        idx += 1
        cache[idx] = cache[idx-1] * idx

        if idx == N:
            break
    return cache[idx]

N = int(input())
print(factorial(N))