n = int(input())
path = list(map(str.upper, input().split()))

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ["L", "R", "U", "D"]

x, y = 1, 1

for p in path:
    for i in range(len(move)):
        if p == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)



# U R D L
# x, y = 1, 1
# for p in path:
#     if p == "U":
#         if x == 1:
#             continue
#         x -= 1
#     if p == "R":
#         if y == len(path):
#             continue
#         y += 1
#     if p == "D":
#         if x == len(path):
#             continue
#         x += 1
#     if p == "L":
#         if y == 1:
#             continue
#         y -= 1

# print(x, y)