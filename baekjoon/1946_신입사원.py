"""
5
3 2
1 4
4 1
2 3
5 5

"""
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    array = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        array.append((a, b))
    array.sort()

    max_val = array[0][1]  # 서류 1둥의 면접 등수
    answer = 1
    for i in range(1, N):
        if max_val > array[i][1]:
            max_val = array[i][1]
            answer += 1
    print(answer)
