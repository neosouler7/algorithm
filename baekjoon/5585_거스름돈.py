"""
380
"""

N = int(input())
N = 1000 - N
A = [500, 100, 50, 10, 5, 1]

answer = 0
for a in A:
    if a > N:
        continue
    answer += N // a
    N -= (N // a) * a
print(answer)