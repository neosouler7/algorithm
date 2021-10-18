"""
2
1 3 1 2
10 2

3
1 3 1 2
10 2 2 1
2 2


6
   1         2                    3
A  1         10                   2
     1, 2        2,1 
B  3         2                    2

   1        11, 15 -> 11          13, 7 -> 7
   3        5, 4   -> 4           6, 14 -> 6  => 6


4
    1      2
A   1      10 -> min(11, 14): 11
     1, 2
B   3      2 -> min(5, 4): 4


comment)
dp !!!!!!!!

"""
import sys
N = int(sys.stdin.readline().rstrip())
work = [[0 for _ in range(N)] for _ in range(2)]
move = [[0 for _ in range(N)] for _ in range(2)]

for k in range(N-1):
    target = list(map(int, sys.stdin.readline().rstrip().split()))
    for i, t in enumerate(target):
        p, q = i // 4, i % 4
        if q == 0:
            work[0][k] = t
        if q == 1:
            work[1][k] = t
        if q == 2:
            move[0][k] = t
        if q == 3:
            move[1][k] = t
final_work = list(map(int, sys.stdin.readline().rstrip().split()))
work[0][N-1], work[1][N-1] = final_work[0], final_work[1]
# for w in work:
#     print(w)
# for w in move:
#     print(w)


for j in range(1, N):
    for i in [0, 1]:  # A, B라인
        other = abs(1-i)
        work[i][j] = min(work[i][j-1], work[other][j-1] + move[other][j-1]) + work[i][j]

print(min(work[0][N-1], work[1][N-1]))