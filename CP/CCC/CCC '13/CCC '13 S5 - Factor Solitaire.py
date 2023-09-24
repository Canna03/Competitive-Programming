cost = 0

n = int(input())

while n > 1:
    for i in range(2, n + 3):
        if n % i == 0:
            cost = cost + (n - (n//i)) // (n//i)
            n = n - n // i
            break


print(cost)