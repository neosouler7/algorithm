"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

"""
N = int(input())
array = []
for _ in range(N):
    a, b = map(int, input().split())
    array.append((a, b))
array.sort(key=lambda x:(x[1], x[0]))

answer = 0
now = 0
for a in array:
    start, end = a
    if start >= now:
        now = end
        answer += 1
print(answer)