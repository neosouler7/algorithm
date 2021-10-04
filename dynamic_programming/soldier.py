"""
출처: 나동빈 이코테2021
내용: -
메모: -
"""

n = int(input())
array = list(map(int, input().split()))

def soldier(array):
    count = 0
    for a, b in zip(array, array[1:]):
        if b > a:
            count += 1
    return count


print(soldier(array))

"""
7
15 11 4 8 5 2 4
"""