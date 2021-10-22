"""
0 - 4
1 - 9
2 - 25

comment)
재귀 or DP(caching) 두 가지 방법 가능 예상.
그 중 개수가 16개로 제한되어, caching로 해결.
"""


dp = [0] * 16
dp[0] = 2

def solution(n):
    if n == 0:
        return dp[n]
    for i in range(1, n+1):
        dp[i] = (dp[i-1] - 1) * 2 + 1
    return dp[n]**2

N = int(input())
print(solution(N))
