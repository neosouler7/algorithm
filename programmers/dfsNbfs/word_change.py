"""
출처: 프로그래머스 > DFS/BFS > 단어 변환
내용: -
메모: -
"""

def dfs(begin, target, words, visited):
    stack = [begin]
    count = 0
    while stack:
        current = stack.pop()
        if current == target:
            return count
        
        for i in range(len(words)):
            if visited[i] == 1:
                continue
            if len(set(current)-set(words[i])) == 1:
                visited[i] = 1
                stack.append(words[i])
        count += 1

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    visited = [0] * len(words)
    answer = dfs(begin, target, words, visited)
    return answer



def dfs(begin, target, words, visited):
    count = 0
    stack = [begin]
    while stack:
        current = stack.pop()
        if current == target:
            return count
        
        for i in range(len(words)):
            if visited[i] == 1:
                continue
            if len(set(current) - set(words[i])) == 1:
                visited[i] = 1
                stack.append(words[i])
        count += 1

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [0] * len(words)
    answer = dfs(begin, target, words, visited)

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))