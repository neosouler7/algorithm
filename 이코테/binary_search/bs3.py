"""
출처: 나동빈 이코테2021
내용: 떡볶이
메모: -
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))

def dduckbokki(array, n, m):
    array.sort()

    h = array[0]
    while True:
        length_sum = 0
        for i in range(len(array)):
            p = array[i] // h
            q = array[i] % h
            length_sum += q if p > 0 else 0

        if length_sum <= m:
            return h
        
        h += 1


print(dduckbokki(array, n, m))

"""
적어도 6만큼을 가져가기 위한 최적 절단기 높이
-> 10 15 17 19

10 -> 0 5 7 9 => 21
11 -> 8 4 

4 6
19 15 10 17
"""