"""
2 3 2

comment)
런타임 에러 때문에 몇번 시도하다가,
나머지는 나머지들의 연산으로도 충분하다는 예전 공부 기억이 떠오름
"""


K, P, N = map(int, input().split())
N *= 10
MOD = 1000000007
def solution(N):
    if N <= 1:
        return P ** N % MOD
    if N % 2 == 0:
        return (solution(N//2) ** 2) % MOD
    elif N % 2 == 1:
        return (P * solution(N//2) ** 2) % MOD

print((K * solution(N)) % 1000000007)