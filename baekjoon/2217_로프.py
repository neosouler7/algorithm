"""
2
10
15
"""
N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)

answer = [0] * N
for i, a in enumerate(array):
    answer[i] = a * (i+1)
print(max(answer))