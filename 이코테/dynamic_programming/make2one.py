"""
출처: 나동빈 이코테2021
내용: 
메모: 발견적 추론이 최선이 아닌가... 어렵다
"""

def make2one(x):
    d = [0] * 30001
    for i in range(2, x+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)

    return d[x]


x = int(input())
print(make2one(x))

""" => 3
26
"""