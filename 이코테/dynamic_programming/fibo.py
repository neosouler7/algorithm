"""
출처: 나동빈 이코테2021
내용: 피보나찌 수열(with 동적)
메모: 최적 부분 구조 / 중복되는 부분 문제일 시 caching하여 해결
"""

# def fibo(x):
#     if x in [1, 2]:
#         return 1
#     return fibo(x-1) + fibo(x-2)

# d = [0] * 100
# def fibo(x):
#     if x in [1, 2]:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = d[x-1] + d[x-2]
#     return fibo(x-1) + fibo(x-2)

def fibo(x):
    n = 99
    d = [0] * 100
    d[0], d[1] = 1, 1
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    
    return d[x-1]

print(fibo(10))