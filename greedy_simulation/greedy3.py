n = int(input())
data = sorted(list(map(int, input().split())), reverse=False)

group = 0
count = 0
for d in data:
    count += 1
    if count >= d:
        group += 1
        count = 0

print(group)
