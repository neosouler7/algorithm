"""
출처: 나동빈 이코테2021
내용: -
메모: -
"""


def mining(input, row, column):
    # array[i][j] = i, j에 존재하는 금의 양
    # dp[i][j] = i, j에서의 dp

    # input -> array 변환
    array = list()
    for i in range(row):
        array.append(input[column*i:column*(i+1)])

    # dp 생성 및 첫 열 초기화
    dp = [[0 for _ in range(column)] for _ in range(row)] 
    for i in range(len(input)):
        if i % column == 0:
            dp[i//column][0] = input[i]

    print(dp)
    print('---------')


    return 1


N = int(input())
for i in range(N):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    print(mining(array, n, m))

"""
1 3 3 2
2 1 4 1 
0 6 4 7


1
3 4
1 3 3 2 2 1 4 1 0 6 4 7


4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""