"""
"""

MAX = 10000

def d(n):
    s = 0
    for a in str(n):
        s += int(a)
    return n + s

def main():
    l = list()
    i = 1
    while True: 
        r = d(i)
        if i > MAX:
            break
        i += 1
        l.append(r)
    for a in sorted(list(set(list(range(1,MAX+1))) - set(l))):
        print(a)
    
main()