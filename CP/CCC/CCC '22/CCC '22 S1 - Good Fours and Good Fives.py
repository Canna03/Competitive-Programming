def x(n: int):
    if n < 4 or n == 6 or n == 7 or n == 11:
        return 0
    elif n < 19:
        return 1


    while n % 5 != 0:
        n -= 4
    return((n // 5) // 4 + 1)
    
print(x(int(input())))