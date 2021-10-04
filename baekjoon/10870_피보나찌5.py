def fibo(N):
    return N if N in [0, 1] else fibo(N-2) + fibo(N-1)

N = int(input())
print(fibo(N))