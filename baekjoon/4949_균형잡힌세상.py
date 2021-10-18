"""
[ first in ] ( first out ).

"""
import sys
while True:
    ss = sys.stdin.readline().rstrip()
    if ss == ".":
        break
    
    stack = []
    flag = True
    for s in ss:     
        if s in ["(", "["]:
            stack.append(s)
        if s == ")":
            if len(stack) == 0 or stack[-1] == "[":
                flag = False
                break
            elif stack[-1] == "(":
                stack.pop()
        if s == "]":
            if len(stack) == 0 or stack[-1] == "(":
                flag = False
                break
            elif stack[-1] == "[":
                stack.pop()
    if flag and len(stack) == 0:
        print("yes")
    else:
        print("no")
