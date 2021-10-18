import sys

stack1 = list(map(str, sys.stdin.readline().rstrip()))
stack2 = []
for _ in range(int(sys.stdin.readline().rstrip())):
    a = list(map(str, sys.stdin.readline().rstrip().split()))
    if a[0] == "L":  # 왼쪽 이동
        if stack1:
            stack2.append(stack1.pop())
    if a[0] == "D":  # 오른쪽 이동
        if stack2:
            stack1.append(stack2.pop())
    if a[0] == "B":  # 커서 왼쪽의 문자 삭제
        if stack1: 
            stack1.pop()
    if a[0] == "P":  # 커서 왼쪽에 문자 추가
        stack1.append(a[1])
print(''.join(stack1) + ''.join(stack2[::-1]))
