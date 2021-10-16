position = input()

y_all = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x, y = int(position[1]), y_all.index(position[0])+1

count = 0
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)


