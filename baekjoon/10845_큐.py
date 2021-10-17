"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front


push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys
from collections import deque

queue = deque([])
for _ in range(int(sys.stdin.readline())):
    c = list(map(str, sys.stdin.readline().split()))
    if c[0] == "push":
        queue.append(c[1])
    if c[0] == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    if c[0] == "size":
        print(len(queue))
    if c[0] == "empty":
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    if c[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    if c[0] == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)