"""
2 3 2

comment)
런타임 에러 때문에 몇번 시도하다가,
나머지는 나머지들의 연산으로도 충분하다는 예전 공부 기억이 떠오름
"""


K, P, N = map(int, input().split())

def solution(K, P, N):
    if N == 0:
        return K % 1000000007
    temp = K
    for _ in range(N):
        answer = temp * P % 1000000007
        temp = answer
    return answer 

print(solution(K, P, N))