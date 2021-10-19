"""
comment)
dp = 자료구조 + 점화식 + 초기화
"""

import sys

def fibo(x):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if x >= len(zero):
        for i in range(len(zero), x+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[x], one[x])

for _ in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    fibo(a)

# cnt_0, cnt_1 = 0, 0
# def fibo(x):
#     if x == 0:
#         global cnt_0
#         cnt_0 += 1
#         return 0
#     elif x == 1:
#         global cnt_1
#         cnt_1 += 1
#         return 1
#     else:
#         return fibo(x-2) + fibo(x-1)

# for _ in range(int(sys.stdin.readline().rstrip())):
#     a = int(sys.stdin.readline().rstrip())
#     fibo(a)
#     print(cnt_0, cnt_1)
#     cnt_0, cnt_1 = 0, 0