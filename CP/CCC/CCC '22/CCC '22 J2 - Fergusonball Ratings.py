n = int(input())
m = n
for i in range(n):
    if int(input()) * 5 - int(input()) * 3 > 40:
        m -= 1

if m == 0:
    print(str(n) + "+")
else:
    print(n-m)
