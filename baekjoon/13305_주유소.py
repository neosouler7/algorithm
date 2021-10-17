"""
4
2 3 1
5 2 4 1

도시 개수
도시 간 거리
도시 별 주유소

Comment)
가장 우측 도시를 제외하고(주유를 할 일이 없으니)
이전 도시의 주유소 가격보다 
비싸면 -> 기존 유지
저렴하면 -> 대체 
"""

N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

price = oil[0]
answer = price * road[0]
for i in range(1, len(oil[:-1])):  # 마지막 도시 제외
    if oil[i] <= price:
        price = oil[i]
    answer += price * road[i]
print(answer)