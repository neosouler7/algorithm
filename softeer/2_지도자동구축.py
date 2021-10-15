"""
0 - 4
1 - 9
2 - 25

comment)
재귀 or DP 두 가지 방법 가능 예상.
그 중 개수가 16개로 제한되어, dp로 해결.
"""


dp = [0] * 16
dp[0] = 2

def solution(n):
    if n == 0:
        return dp[n]
    for i in range(n):
        a = (dp[i] - 1) * 2 + 1
        dp[i+1] = a
    return dp[n]**2

N = int(input())
print(solution(N))
