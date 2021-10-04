n, k = map(int, input().split())

count = 0
while True:
    if n == 1:
        break
    n = n // k if n % k == 0 else n - 1
    count += 1

print(count)