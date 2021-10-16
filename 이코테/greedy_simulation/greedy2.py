data = input()

result = int(data[0])
for i, _ in enumerate(data):
    v = int(data[i])
    if result <= 1 or v <= 1:
        result += v
    else:
        result *= v

print(result)