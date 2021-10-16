"""
출처: 나동빈 이코테2021
내용: -
메모: 어렵다... 화폐 단위 / 총 금액 두 개의 지표를 기준으로 비교.
"""

def currency(array, n, m):
    d = [10001] * (m+1)
    d[0] = 0
    for i in range(n):
        for j in range(array[i], m+1):
            if d[j-array[i]] != 10001:
                d[j] = min(d[j], d[j-array[i]] + 1)
    return -1 if d[m] == 100001 else d[m]

n, m = map(int, input().split())
array = list()
for i in range(n):
    array.append(int(input()))

print(currency(array, n, m))

"""
2 15
2
3
"""
