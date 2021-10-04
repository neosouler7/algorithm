array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(array)


from collections import Counter

l = list()
for k, v in sorted(Counter(array).items(), key=lambda x:x[0]):
    l.append(v)

for i, v in enumerate(l):
    for j in range(v):
        print(str(i), end = " ")