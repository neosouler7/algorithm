while True:
    try:
        a, b = map(int, input().split())
    except Exception as e:
        break
    print(a+b)