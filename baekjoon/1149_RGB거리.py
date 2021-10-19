"""
3
26 40 83
49 60 57
13 89 99

comment)
dp!!

dp[i] = dp[i] + i-1행에서 이전 열 제외 중 min
"""
import sys
n = int(sys.stdin.readline().rstrip())
dp = []
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(1, n):
    dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = dp[i][2] + min(dp[i-1][1], dp[i-1][0])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))