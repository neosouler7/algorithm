"""
100 2
90 1
70 2

comment)
greedy
"""

W, N = map(int, input().split())
array = [0] * (N+1)
for _ in range(N):  # sort!
    m, p = map(int, input().split())
    array[p] += m  # 중복입력이 있을 수도 있다...

answer = 0
p = len(array) - 1
while W > 0:
    weight = array[p]
    if W < weight:
        answer += W * p
        W -= W
    else:
        answer += weight * p
        W -= weight
    p -= 1

print(answer)