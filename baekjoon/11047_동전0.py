"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

"""

N, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort(reverse=True)


answer = 0
for a in array:
    if a > K:
        continue
    if K // a > 0:
        answer += (K // a)
        K -= (K // a) * a

print(answer)