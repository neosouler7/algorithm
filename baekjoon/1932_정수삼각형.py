"""
dp!! 나열하고 규칙을 찾는다

배열상으로는 j 혹은 j+1

양쪽에 있는 값들은 이전값 그대로 더하고
아닌 것들은 이전 행에서 큰값을 취해 더한다.

"""
import sys
n = int(sys.stdin.readline().rstrip())
dp = []
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif i == j:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i-1][j-1])
    k += 1
print(max(dp[n-1]))