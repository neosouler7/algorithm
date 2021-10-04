"""
출처: 프로그래머스 > Greedy > 조이스틱
내용: -
메모: -
"""

A = "A"
Z = "Z"

def solution(name):
    change = [min(ord(n) - ord("A"), ord("Z") - ord(n) + 1) for n in name]
    answer, idx = 0, 0

    while True:
        answer += change[idx]
        change[idx] = 0 
        if sum(change) == 0:
            return answer

        left, right = 1, 1     
        while change[idx-left] == 0:
            left += 1
        while change[idx+right] == 0:
            right += 1
        
        idx += -left if right > left else right
        answer += left if right > left else right

name = "JAZ"
print(solution(name))
