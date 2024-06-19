def execute(s: str, a: int, b: int):
    instruction = s.split(' ')
    if instruction[0] == '7':
        return (-1)
    if instruction[0] == '1':
        if instruction[1] == 'A':
            a = int(instruction[2])
        else:
            b = int(instruction[2])
    elif instruction[0] == '2':
        if instruction[1] == 'A':
            print(a)
        else:
            print(b)
    elif instruction[0] == '3':
        if instruction[1] == 'A':
            if instruction[2] == 'A':
                a = a + a
            else:
                a = a + b
        else:
            if instruction[2] == 'A':
                b = b + a
            else:
                b = b + b
    elif instruction[0] == '4':
        if instruction[1] == 'A':
            if instruction[2] == 'A':
                a = a * a
            else:
                a = a * b
        else:
            if instruction[2] == 'A':
                b = b * a
            else:
                b = b * b
    elif instruction[0] == '5':
        if instruction[1] == 'A':
            if instruction[2] == 'A':
                a = a - a
            else:
                a = a - b
        else:
            if instruction[2] == 'A':
                b = b - a
            else:
                b = b - b
    elif instruction[0] == '6':
        if instruction[1] == 'A':
            if instruction[2] == 'A':
                a = a // a
            else:
                a = a // b
        else:
            if instruction[2] == 'A':
                b = b // a
            else:
                b = b // b
    return a, b
    
def solve():
    a = 0
    b = 0
    s = input()
    t = execute(s, a, b)
    while t != (-1):
        s = input()
        a, b = t
        t = execute(s, a, b)
    return

solve()