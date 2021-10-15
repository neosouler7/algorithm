"""
5 3
10 50 20 70 100
1 3
3 4
1 5

comment)
string slice!
"""

N, K = map(int, input().split())
array = list(map(int, input().split()))
interval = list()
for _ in range(K):
    a, b = map(int, input().split())
    interval.append((a-1, b-1))  # index

for x, y in interval:
    print('{:.2f}'.format(round(sum(array[x:y+1]) / (y-x+1), 2)))