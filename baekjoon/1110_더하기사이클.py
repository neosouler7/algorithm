def solution(N):
    origin = N
    count = 0
    while True:
        count += 1
        p, q = N // 10, N % 10
        N = q * 10 + ((p+q) % 10)      
        if origin == N:
            return count
    

N = int(input())
print(solution(N))