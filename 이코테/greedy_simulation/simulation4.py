data = input()

alpha, sum = list(), 0
for d in data:
    if d.isalpha():
        alpha.append(d)
    else:
        sum += int(d)

print(f'{"".join(sorted(alpha))}{sum}')