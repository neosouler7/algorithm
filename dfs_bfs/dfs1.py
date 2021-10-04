# 각 노드가 연결된 정보와 방문 이력 정보를 작성
graph = [
    [],  # 노드가 1번부터 시작하니
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
visited = [False] * len(graph)

path = list()
def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end = "")
    path.append(str(v))
    if all(visited[1:]):
        print(' '.join(path))
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
