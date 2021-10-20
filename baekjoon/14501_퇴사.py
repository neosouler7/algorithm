"""
comment)
dp, 갈라치기를 잘 해야하는데... 쉽지 않군
"""

import sys

N = int(sys.stdin.readline().rstrip())
t, p = list(), list()
for _ in range(N):
    temp = list(map(int,  sys.stdin.readline().rstrip().split()))
    t.append(temp[0])
    p.append(temp[1])
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + t[i] > N:  # i일에 상담하는 것이 퇴사일을 넘기면, 상담을 하지 않고
        dp[i] = dp[i+1]
    else:  # 상담하는 경우, i일에 상담하는 경우 vs 상담을 안하는 것 중 큰 것
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

print(dp[0])