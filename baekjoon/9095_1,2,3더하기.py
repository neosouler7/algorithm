"""
3

4
7
10

7 44 274

comment)
dp + 런타임에러 때문에 재귀!!
"""

# dp[n] = dp[n-1] * 2 + 1 (n >= 3, dp[0]=dp[1]=dp[2]=1)

# import sys
# for _ in range(int(sys.stdin.readline().rstrip())):
#     n = int(sys.stdin.readline().rstrip())
#     dp = [0] * (n+1)
#     dp[1], dp[2], dp[3] = 1, 2, 4
#     for i in range(4, n+1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#     print(dp[n])


import sys
sys.setrecursionlimit(100000)

def dp(x):
    if x == 1:
        return 1 
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return dp(x-3) + dp(x-2) + dp(x-1)

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    print(dp(n))