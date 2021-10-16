"""
55-50+40+10-30

"""

array = input().split('-')
answer = 0
for a in array[0].split('+'):
    answer += int(a)
for a in array[1:]:
    for b in a.split('+'):
        answer -= int(b)

print(answer)