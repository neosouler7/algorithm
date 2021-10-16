"""
출처: 프로그래머스 > Greedy > 체육복
내용: -
메모: -
"""
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
        
    return n - len(set_lost)

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))