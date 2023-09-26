for t in range(int(input())):
    n = int(input())
    m = []
    b = []
    l = []
    for i in range(n):
        m.append(int(input()))
    a = 1
    while m or b:
        if not m and b and b[-1] != a:
            break
        if b and b[-1] == a:
            l.append(b.pop())
            a += 1
        elif m[-1] != a:
            b.append(m.pop())
        else:
            l.append(m.pop())
            a += 1
    if not b:
        print("Y")
    else:
        print("N")