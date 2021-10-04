"""
출처: Softeer > 연습문제 > Garage Game
내용: -
메모: -
"""

def solution(n, array):
    print(n)
    print(array)

n = int(input())
array = []
for i in range(n * 3):
    array.append(list(map(int, input().split())))

solution(n, array)


"""
2
1 1
2 2
1 1
3 3
4 4
1 2
"""