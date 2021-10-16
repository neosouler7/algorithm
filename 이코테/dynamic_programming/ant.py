"""
출처: 나동빈 이코테2021
내용: 전체를 아우르는 기준점을 잘 찾자.
메모: -
"""

n = int(input())
array = list(map(int, input().split()))

def ant(n, array):
    d = [0] * 100
    d[0] = array[0]
    d[1] = max(array[0], array[1])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2]+array[i])
    return d[n-1]


print(ant(n, array))

"""
=> 8
4
1 3 1 5
"""