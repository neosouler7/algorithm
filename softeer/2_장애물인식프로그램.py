"""
7
1110111
0110101
0110101
0000100
0110000
0111110
0110000

comment)
dfs count + sub_count
"""

N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input())))
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
sub_count = 0
sub_count_list = []

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        if visited[nx][ny]:
            continue
        if array[nx][ny] == 1:
            dfs(nx, ny)
            global sub_count
            sub_count += 1
    
for i in range(N):
    for j in range(N):
        if not visited[i][j] and array[i][j] == 1:
            sub_count = 1
            dfs(i, j)
            sub_count_list.append(sub_count)
            count += 1

sub_count_list.sort()
print(count)
for s in sub_count_list:
    print(s)
