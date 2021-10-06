sub_count = 0

def dfs(x, y, N, array, visited):
    visited[x][y] = True
    global sub_count
    sub_count += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue

        if visited[nx][ny] or array[nx][ny] == 0:
            continue

        dfs(nx, ny, N, array, visited)


def solution(N, array):
    visited = [[False for _ in range(N)] for _ in range(N)]
    answer = list()
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and array[i][j] == 1:
                global sub_count
                sub_count = 0
                dfs(i, j, N, array, visited)
                answer.append(sub_count)
    answer.sort()
    return f'{len(answer)} {" ".join([str(a) for a in answer])}'

N = int(input())
array = list()
for i in range(N):
    array.append(list(map(int, input())))

print(solution(N, array))

"""
dfs subcount order + length!!


7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""