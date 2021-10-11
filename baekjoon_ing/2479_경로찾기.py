from collections import defaultdict, deque

def solution(N, K, A, B, graph):
    # print(N, K, A, B)
    # print(graph)
    target_dist = 0
    for a, b in zip(array[A-1], array[B-1]):
        if a != b:
            target_dist += 1
    visited = [False] * (N+1)
    start = A
    queue = deque([start])
    answer = list()
    answer.append(start)
    while queue:
        # print(queue)
        node = queue.popleft()
        # print(node)
        # print(n, node)
        if node == B:
            # answer.append(B)
            return ' '.join([str(a) for a in answer])
        visited[node] = True

        for i in graph[node]:
            if not visited[i[0]] and i[1] == 1:  # only if 1
                queue.append(i[0])
                answer.append(i[0])
                break
        # print('--------')
    return -1


N, K = map(int, input().split())
array = list()
for i in range(N):
    array.append(str(input()))
graph = defaultdict(list)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        distance = 0
        for a, b in zip(array[i], array[j]):
            if a != b:
                distance += 1
        graph[i+1].append((j+1, distance))  # key: from / value: (to, distance)

A, B = map(int, input().split())

print(solution(N, K, A, B, graph))

"""
5 3
000
111
010
110
001
1 2
"""