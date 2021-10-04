array = [1, 5, 3, 8, 4, 4, 6]
print(array)

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] >= array[j]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i]  # swap

print(array)