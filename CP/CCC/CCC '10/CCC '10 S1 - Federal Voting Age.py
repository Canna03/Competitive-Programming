for i in range(int(input())):
    x = [int(a) for a in input().split(' ')]
    if x[0] < 1989:
        print('Yes')
    elif x[0] > 1989:
        print('No')
    elif x[1] < 2:
        print('Yes')
    elif x[1] > 2:
        print('No')
    elif x[2] < 28:
        print('Yes')
    else:
        print('No')