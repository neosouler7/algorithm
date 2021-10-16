"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=411

모든 점에 대하여
대각선 이동까지 허용해주는 dfs를 돌리고,
각 dfs마다 2개 이상의 변이 0과 접하면 0으로 바꿔준다. (dfs돌린 수만큼)

그리고 모든 값이 다 0으로 될 때까지 이를 반복한다.
종료조건은 dfs 돌 경우가 없을 때!

Q. 근데 안쪽에 있는 얼음을 어떻게 구분하지?
"""

N, M = map(int, input().split())
array = list()
for _ in range(N):
    array.append([bool(x) for x in list(map(int, input().split()))])


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x, y, visited, array):
    visited[x][y] = True
    global change_target


    




def solution():
    answer = 0
    while True:
        visited = [[False for _ in range(M)] for _ in range(N)]
        change_target = []  # 얼음 녹을 후보군을 정하고
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and array[i][j]:
                    dfs(i, j, visited, array)
                    answer += 1
                    # change array

        if len(change_target) == 0:  # 얼음 녹을 대상이 없다면
            return answer

print(solution())
