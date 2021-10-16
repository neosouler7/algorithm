"""
출처: 프로그래머스 > DFS/BFS > 네트워크
내용: -
메모: -
"""

def solution(n, computers):
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)

    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer

"""
[1, 1, 0]
[1, 1, 0]
[0, 0, 1]


[1, 1, 0]
[1, 1, 1]
[0, 1, 1]
"""

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))