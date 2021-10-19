"""
comment)
최초 greedy로 접근하였으나, dp!
"""
# dp[n] = min(dp[n//3]+1, dp[n//2]+1, dp[n-1]+1)
import sys
N = int(sys.stdin.readline().rstrip())
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[N])


# greedy -> 반례 10
# import sys
# N = int(sys.stdin.readline().rstrip())
# count = 0
# while N > 0:
#     if N % 3 == 0:
#         N = N // 3
#     elif N % 2 == 0:
#         N = N // 2
#     else:
#         N -= 1
#     count += 1
# print(count)