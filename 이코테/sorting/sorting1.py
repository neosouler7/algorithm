n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a = sorted(a, reverse=False)
b = sorted(b, reverse=True)

for i in range(k):
    if b[i] > a[i]:
        b[i], a[i] = a[i], b[i]

print(sum(a))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""