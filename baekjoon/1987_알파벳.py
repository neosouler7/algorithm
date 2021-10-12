"""
2 4
CAAB
ADCB
"""

R, C = map(int, input().split())
array = list()
for _ in range(R):
    array.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = (0, 0, array[0][0])
queue = set([start])

count = 1
while queue:
    x, y, visited = queue.pop()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if array[nx][ny] not in visited:
            new_visited = visited + array[nx][ny]
            queue.add((nx, ny, new_visited))
            count = max(count, len(new_visited))
print(count)