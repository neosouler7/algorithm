"""
출처: 프로그래머스 > 정렬 > H-Index
내용: -
메모: -
"""


def solution(citations):
    citations.sort(reverse=True)  # 6 5 3 1 0
    l = len(citations)
    for i in range(l):
        if citations[i] <= i:
            return i
    return l

citations = [3, 0, 6, 1, 5]
print(solution(citations))