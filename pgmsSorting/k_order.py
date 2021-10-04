"""
출처: 프로그래머스 > 정렬 > k번째 수
내용: -
메모: 매우 쉬움...
"""


def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        answer.append(sorted(array[i-1:j])[k-1])
    return answer



# [5, 6, 3]
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))