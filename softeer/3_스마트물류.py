"""
20 1
HHPHPPHHPPHPPPHPHPHP

greedy 

각 로봇 좌표로부터, 
-K ~ K 만큼 돌면서
가장 멀리있는 것부터 get. (값 초기화)

그리고 get 하면서 count += 1

"""

N, K = map(int, input().split())
array = list(map(str, input()))

answer = 0
for i, a in enumerate(array):  # P(로봇)와 H(부품)
    if a == "P":  # 로봇이면,
        for j in range(i-K, i+K+1):  # ~K ~ +K
            if i == j:  # 로봇 위치
                continue
            if j < 0 or j >= N:  # 이탈
                continue
            if array[j] == "H":  # 부품이면, 그 부품 집고 해당 로봇 종료
                array[j] = 0
                answer += 1
                break
print(answer)
