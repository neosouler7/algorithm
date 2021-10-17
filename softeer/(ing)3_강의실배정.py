"""
3
1 3
2 4
3 5

6
3 5
1 3
1 2
1 4
2 4
2 3

https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=392

Q. 런타임 에러... 무얼 더 줄일 수 있을까

"""

import sys
input = sys.stdin.readline

N = int(input())

array = [[0]*2 for _ in range(N)] 
for i in range(N): 
    s, e = map(int, sys.stdin.readline().split()) 
    array[i][0] = s 
    array[i][1] = e 

array.sort(key = lambda x: (x[1], x[0])) 

cnt = 1 
end_time = array[0][1] 
for i in range(1, N): 
    if array[i][0] >= end_time: 
        cnt += 1 
        end_time = array[i][1] 
print(cnt)




# import sys
# input = sys.stdin.readline

# N = int(input())
# array = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     array.append((a, b))

# array.sort(key=lambda x:(x[1], x[0]))

# now = 0
# count = 0
# for a in array:
#     start, end = a
#     if start >= now:
#         now = end
#         count += 1
# print(count)

"""
- 종료 시간이 짧은 것 부터 정렬 (종료 시간이 같다면 시작 시간이 짧은 순으로 정렬)
- 1) 반복문을 돌면서 현재 시간보다 시작 시간이 작다면 pass
- 2) 아니라면 count + 1해주고 현재 시간 갱신
- 3) 답은 count
"""
