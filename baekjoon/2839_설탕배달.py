"""

greedy

5의 배수가 될 떄까지 3만큼 뺴자!!
"""
N = int(input())

answer = 0
while True:
    if N % 5 == 0:
        answer += (N // 5)
        break
    N -= 3
    answer += 1
    if N < 0:
        answer = -1
        break
print(answer)