"""
5
1 1 1 6 0
2 7 8 3 1

"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=False)

answer = 0
for a, b in zip(A, B):
    answer += a * b
print(answer)