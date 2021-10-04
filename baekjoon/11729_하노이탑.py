def hanoi(N, start, to, via):
    if N == 1:
        answer.append([start, to])
    else:
        hanoi(N-1, start, via, to)
        answer.append([start, to])
        hanoi(N-1, via, to, start)

answer = []
hanoi(int(input()), 1, 3, 2)
print(len(answer))
for a in answer:
    print(f'{a[0]} {a[1]}')
