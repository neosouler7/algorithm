"""

3
((
))
())(()

6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

"""

for _ in range(int(input())):
    ss = list(map(str, input()))
    count = 0
    for s in ss:
        if s == "(":
            count += 1
        if s == ")":
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")