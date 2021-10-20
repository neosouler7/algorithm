"""
comment)
최대값인 13을 안 먹는 반례가 있으므로, dp!
규칙, 즉 점화식을 찾아야함.
숫자를 나열해볼까, 경우를 나열해볼까

6,  10, 13,  9,  8,  1
w1, w2, w3, w4, w5, w6

let dp: "해당 순서까지의 최대값"
dp1 - w1
dp2 - w1+w2
dp3 - w1+w2
    - w1+w3
    - w2+w3
dp4 - w1+w2+w4
    - w1+w3+w4
    - w2+w3

i == 1 -> w1
i == 2 -> w1 + w2
i == 3 -> dp[i-1], dp[i-2] + w[i], dp[i-3] + w[i] + w[i-1]
i == 4 -> dp[i-1], dp[i-2] + w[i], dp[i-3] + w[i] + w[i-1]
"""

import sys
n = int(sys.stdin.readline().rstrip())
grape = [0]  # n+1
for _ in range(n):
    grape.append(int(sys.stdin.readline().rstrip()))
dp = [0] * (n+1)

dp[1] = grape[1]
if n > 1:
    dp[2] = grape[1] + grape[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + grape[i], dp[i-3] + grape[i] + grape[i-1])
print(max(dp))
