array = [1, 5, 3, 8, 4, 4, 6]
print(array)

for i in range(len(array)):
    for j in range(len(array[:i])):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

print(array)


array = [1, 5, 3, 8, 4, 4, 6]
print(array)
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)